import numpy as np
import matplotlib.pyplot as plt
import time

# ----------------------------
# Grid parameters
# ----------------------------
Nx, Ny = 100, 100
Lx, Ly = 20.0, 20.0
dx, dy = Lx / Nx, Ly / Ny
x = np.linspace(-Lx/2, Lx/2, Nx)
y = np.linspace(-Ly/2, Ly/2, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

# Position of nuclei
atom_pos = [(-3.33, 0.0), (3.33, 0.0)]
Z = 6

# ----------------------------
# External Potential
# ----------------------------
def compute_external_potential(X, Y, atom_pos, Z):
    V = np.zeros_like(X)
    for (x0, y0) in atom_pos:
        r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-10
        V += Z / (4.0 * r)
    return V

# ----------------------------
# Laplace operator (dense)
# ----------------------------
def create_laplacian(Nx, Ny, dx, dy):
    N = Nx * Ny
    L = np.zeros((N, N))

    def idx(i, j):
        return (i % Nx) + (j % Ny) * Nx

    for j in range(Ny):
        for i in range(Nx):
            center = idx(i, j)
            L[center, center] = -2.0 / dx**2 - 2.0 / dy**2
            L[center, idx(i - 1, j)] = 1.0 / dx**2
            L[center, idx(i + 1, j)] = 1.0 / dx**2
            L[center, idx(i, j - 1)] = 1.0 / dy**2
            L[center, idx(i, j + 1)] = 1.0 / dy**2
    return L

# ----------------------------
# Vectorized Hartree potential
# ----------------------------
def compute_hartree_potential_vectorized(rho, dx, dy, epsilon=1e-4):
    Nx, Ny = rho.shape
    x = np.linspace(-Nx/2*dx, Nx/2*dx, Nx)
    y = np.linspace(-Ny/2*dy, Ny/2*dy, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')

    # Expand dims for broadcasting
    rx = X[:, :, np.newaxis, np.newaxis]
    ry = Y[:, :, np.newaxis, np.newaxis]
    Xp = X[np.newaxis, np.newaxis, :, :]
    Yp = Y[np.newaxis, np.newaxis, :, :]
    rho_expand = rho[np.newaxis, np.newaxis, :, :]

    r_dist = np.sqrt((Xp - rx)**2 + (Yp - ry)**2 + epsilon**2)
    V_H = np.sum(rho_expand / r_dist, axis=(2,3)) * dx * dy
    return V_H

# ----------------------------
# SCF parameters
# ----------------------------
V_ext = compute_external_potential(X, Y, atom_pos, Z)
L = create_laplacian(Nx, Ny, dx, dy)
max_iter = 2
num_states = 6
energy_list = []

# Initial density
V_flat_init = V_ext.flatten()
H_init = -0.5 * L + np.diag(V_flat_init)
eigvals_init, eigvecs_init = np.linalg.eigh(H_init)
eigvecs_init = eigvecs_init[:, :num_states]
psi_init = eigvecs_init.reshape((Nx, Ny, num_states))
rho = np.sum(np.abs(psi_init)**2, axis=2)
tol = 1e-3

# ----------------------------
# SCF loop with timing & bottleneck detection
# ----------------------------
start_total = time.perf_counter()

for it in range(max_iter):
    print(f"\n--- SCF Iteration {it+1} ---")
    start_iter = time.perf_counter()

    # Hartree potential
    start = time.perf_counter()
    V_H = compute_hartree_potential_vectorized(rho, dx, dy)
    time_hartree = time.perf_counter() - start

    # Hamiltonian construction
    start = time.perf_counter()
    V_eff = V_ext + V_H
    H = -0.5 * L + np.diag(V_eff.flatten())
    time_hamiltonian = time.perf_counter() - start

    # Eigenvalue solution
    start = time.perf_counter()
    eigvals_all, eigvecs_all = np.linalg.eigh(H)
    eigvals = eigvals_all[:num_states]
    eigvecs = eigvecs_all[:, :num_states]
    psi = eigvecs.reshape((Nx, Ny, num_states))
    time_eig = time.perf_counter() - start

    # Update density
    rho_new = np.sum(np.abs(psi)**2, axis=2)
    alpha = 0.3
    rho = alpha * rho_new + (1 - alpha) * rho

    total_energy = np.sum(eigvals)
    energy_list.append(total_energy)
    print(f"Energy = {total_energy:.6f}")

    # Print timings
    timings = {"Hartree Potential": time_hartree,
               "Hamiltonian Construction": time_hamiltonian,
               "Eigenvalue Solution": time_eig}
    for key, val in timings.items():
        print(f"  {key}: {val:.4f} s")

    # Identify bottleneck(s)
    max_time = max(timings.values())
    bottlenecks = [k for k,v in timings.items() if v == max_time]
    print("Bottleneck(s):", ", ".join(bottlenecks))

    # Convergence check
    if it > 0:
        delta_E = abs(energy_list[-1] - energy_list[-2])
        if delta_E < tol:
            print(f"Convergence achieved after {it+1} iterations (ΔE = {delta_E:.6f})")
            break

end_total = time.perf_counter()
print(f"\nTotal runtime (vectorized, no sparse): {end_total - start_total:.4f} s")

# ----------------------------
# Visualization
# ----------------------------
plt.figure(figsize=(6,5))
plt.contourf(X, Y, rho, levels=50, cmap='plasma')
plt.colorbar(label='electron density $\\rho(r)$')
plt.title('Converged electron density (Vectorized)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()



# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day9> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day9/DFT_Vectorized.py"

# --- SCF Iteration 1 ---
# Energy = 4.355522
#   Hartree Potential: 2.8431 s
#   Hamiltonian Construction: 1.4600 s
#   Eigenvalue Solution: 172.2527 s
# Bottleneck(s): Eigenvalue Solution

# --- SCF Iteration 2 ---
# Energy = 4.537730
#   Hartree Potential: 2.6793 s
#   Hamiltonian Construction: 1.4073 s
#   Eigenvalue Solution: 169.7678 s
# Bottleneck(s): Eigenvalue Solution

# Total runtime (vectorized, no sparse): 350.4797 s