import numpy as np
import matplotlib.pyplot as plt
import time

# Grid parameters
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
# FUNCTIONS
# ----------------------------
def compute_external_potential(X, Y, atom_pos, Z):
    V = np.zeros_like(X)
    for (x0, y0) in atom_pos:
        r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-10
        V += Z / (4.0 * r)
    return V

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

def compute_hartree_potential(rho, dx, dy, epsilon=1e-4):
    Nx, Ny = rho.shape
    V_H = np.zeros_like(rho)
    x = np.linspace(-Nx/2*dx, Nx/2*dx, Nx)
    y = np.linspace(-Ny/2*dy, Ny/2*dy, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')

    for i in range(Nx):
        for j in range(Ny):
            rx, ry = X[i, j], Y[i, j]
            r_prime_x = X - rx
            r_prime_y = Y - ry
            r_dist = np.sqrt(r_prime_x**2 + r_prime_y**2 + epsilon**2)
            integrand = rho / r_dist
            V_H[i, j] = np.sum(integrand) * dx * dy
    return V_H

# ----------------------------
# MAIN SCF CALCULATION
# ----------------------------
V_ext = compute_external_potential(X, Y, atom_pos, Z)
L = create_laplacian(Nx, Ny, dx, dy)

max_iter = 2
num_states = 6
energy_list = []

# Starting value for density
V_flat_init = V_ext.flatten()
H_init = -0.5 * L + np.diag(V_flat_init)
eigvals_init, eigvecs_init = np.linalg.eigh(H_init)
eigvecs_init = eigvecs_init[:, :num_states]
psi_init = eigvecs_init.reshape((Nx, Ny, num_states))
rho = np.sum(np.abs(psi_init)**2, axis=2)

tol = 1e-3

# ----------------------------
# START TIMER
# ----------------------------
start_time_total = time.perf_counter()

for it in range(max_iter):
    print(f"\n--- SCF Iteration {it+1} ---")
    
    timings = {}
    
    t0 = time.perf_counter()
    V_H = compute_hartree_potential(rho, dx, dy)
    timings["Hartree Potential"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    V_eff = V_ext + V_H
    V_flat = V_eff.flatten()
    H = -0.5 * L + np.diag(V_flat)
    timings["Hamiltonian Construction"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    eigvals_all, eigvecs_all = np.linalg.eigh(H)
    eigvals = eigvals_all[:num_states]
    eigvecs = eigvecs_all[:, :num_states]
    psi = eigvecs.reshape((Nx, Ny, num_states))
    rho_new = np.sum(np.abs(psi)**2, axis=2)
    timings["Eigenvalue Solution"] = time.perf_counter() - t0

    alpha = 0.3
    rho = alpha * rho_new + (1 - alpha) * rho

    total_energy = np.sum(eigvals)
    energy_list.append(total_energy)
    print(f"Energy = {total_energy:.6f}")

    # Identify bottleneck(s)
    max_time = max(timings.values())
    bottlenecks = [name for name, t in timings.items() if t == max_time]
    print("Timings (s):")
    for name, t in timings.items():
        print(f"  {name}: {t:.4f}")
    print("Bottleneck(s):", ", ".join(bottlenecks))

    if it > 0:
        delta_E = np.abs(energy_list[-1] - energy_list[-2])
        if delta_E < tol:
            print(f"Convergence achieved (ΔE = {delta_E:.6f})")
            break

# ----------------------------
# END TIMER
# ----------------------------
end_time_total = time.perf_counter()
print(f"\nTotal runtime (baseline, no optimization): {end_time_total - start_time_total:.4f} s")

# Visualization
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, rho, levels=50, cmap='plasma')
plt.colorbar(label='electron density $\\rho(r)$')
plt.title('Converged electron density after SCF')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day9/Beforeoptimization.py"

# --- SCF Iteration 1 ---
# Energy = 4.355522
# Timings (s):
#   Hartree Potential: 0.6033
#   Hamiltonian Construction: 1.6986
#   Eigenvalue Solution: 171.9258
# Bottleneck(s): Eigenvalue Solution

# --- SCF Iteration 2 ---
# Energy = 4.537730
# Timings (s):
#   Hartree Potential: 0.5397
#   Hamiltonian Construction: 1.3288
#   Eigenvalue Solution: 168.2510
# Bottleneck(s): Eigenvalue Solution

# Total runtime (baseline, no optimization): 344.3840 s