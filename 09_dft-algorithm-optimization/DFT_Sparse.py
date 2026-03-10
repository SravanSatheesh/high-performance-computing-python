import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.sparse import lil_matrix, diags
from scipy.sparse.linalg import eigsh  # for sparse eigenvalue solver

# ----------------------------
# Grid parameters
# ----------------------------
Nx, Ny = 100, 100
Lx, Ly = 20.0, 20.0
dx, dy = Lx / Nx, Ly / Ny
x = np.linspace(-Lx/2, Lx/2, Nx)
y = np.linspace(-Ly/2, Ly/2, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

# ----------------------------
# Nuclei
# ----------------------------
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
# Sparse Laplace Operator
# ----------------------------
def create_sparse_laplacian(Nx, Ny, dx, dy):
    N = Nx * Ny
    diagonals = []

    main_diag = -2.0/dx**2 - 2.0/dy**2
    side_diag_x = 1.0/dx**2
    side_diag_y = 1.0/dy**2

    # 1D flattened Laplacian
    diag = main_diag * np.ones(N)
    diagonals.append(diag)
    
    # neighbors in x-direction
    diagonals.append(side_diag_x * np.ones(N-1))
    diagonals.append(side_diag_x * np.ones(N-1))
    
    # neighbors in y-direction
    diagonals.append(side_diag_y * np.ones(N-Nx))
    diagonals.append(side_diag_y * np.ones(N-Nx))

    offsets = [0, -1, 1, -Nx, Nx]
    L = diags(diagonals, offsets, shape=(N, N), format='lil')
    return L

# ----------------------------
# Hartree Potential
# ----------------------------
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
# SCF parameters
# ----------------------------
max_iter = 2
num_states = 6
tol = 1e-3
energy_list = []

# ----------------------------
# Prepare potentials and Laplacian
# ----------------------------
V_ext = compute_external_potential(X, Y, atom_pos, Z)
L = create_sparse_laplacian(Nx, Ny, dx, dy)

# ----------------------------
# Starting density
# ----------------------------
V_flat_init = V_ext.flatten()
H_init = -0.5 * L + diags(V_flat_init, 0)
eigvals_init, eigvecs_init = eigsh(H_init, k=num_states, which='SA')
psi_init = eigvecs_init.reshape((Nx, Ny, num_states))
rho = np.sum(np.abs(psi_init)**2, axis=2)

# ----------------------------
# MAIN SCF LOOP WITH TIMERS
# ----------------------------
start_total = time.perf_counter()

for it in range(max_iter):
    print(f"\n--- SCF Iteration {it+1} ---")
    iter_start = time.perf_counter()

    # Hartree Potential
    t0 = time.perf_counter()
    V_H = compute_hartree_potential(rho, dx, dy)
    t1 = time.perf_counter()
    time_hartree = t1 - t0

    # Hamiltonian Construction
    t0 = time.perf_counter()
    V_eff = V_ext + V_H
    V_flat = V_eff.flatten()
    H = -0.5 * L + diags(V_flat, 0)
    t1 = time.perf_counter()
    time_hamiltonian = t1 - t0

    # Eigenvalue solution
    t0 = time.perf_counter()
    eigvals_all, eigvecs_all = eigsh(H, k=num_states, which='SA')
    t1 = time.perf_counter()
    time_eigen = t1 - t0

    # Electron density
    psi = eigvecs_all.reshape((Nx, Ny, num_states))
    rho_new = np.sum(np.abs(psi)**2, axis=2)
    alpha = 0.3
    rho = alpha * rho_new + (1 - alpha) * rho

    # Energy
    total_energy = np.sum(eigvals_all)
    energy_list.append(total_energy)
    print(f"Energy = {total_energy:.6f}")

    # Determine bottleneck(s)
    times = {'Hartree Potential': time_hartree,
             'Hamiltonian Construction': time_hamiltonian,
             'Eigenvalue Solution': time_eigen}
    max_time = max(times.values())
    bottlenecks = [k for k, v in times.items() if np.isclose(v, max_time)]
    print("Timings (s):")
    for k, v in times.items():
        print(f"  {k}: {v:.4f}")
    print(f"Bottleneck(s): {', '.join(bottlenecks)}")

    # Convergence check
    if it > 0:
        delta_E = np.abs(energy_list[-1] - energy_list[-2])
        if delta_E < tol:
            print(f"Convergence achieved after {it+1} iterations (ΔE = {delta_E:.6f})")
            break

end_total = time.perf_counter()
print(f"\nTotal runtime (sparse Laplace with detailed timings): {end_total - start_total:.4f} s")

# ----------------------------
# Visualization
# ----------------------------
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, rho, levels=50, cmap='plasma')
plt.colorbar(label='electron density $\\rho(r)$')
plt.title('Converged electron density after SCF (Sparse Laplace)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()


# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day9> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day9/DFT_Sparse.py"

# --- SCF Iteration 1 ---
# Energy = 4.419647
# Timings (s):
#   Hartree Potential: 0.4918
#   Hamiltonian Construction: 0.0088
#   Eigenvalue Solution: 0.2683
# Bottleneck(s): Hartree Potential

# --- SCF Iteration 2 ---
# Energy = 4.966721
# Timings (s):
#   Hartree Potential: 0.4952
#   Hamiltonian Construction: 0.0133
#   Eigenvalue Solution: 0.4328
# Bottleneck(s): Hartree Potential

# Total runtime (sparse Laplace with detailed timings): 1.7144 s