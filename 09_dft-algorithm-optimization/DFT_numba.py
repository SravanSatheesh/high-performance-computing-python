import numpy as np
import matplotlib.pyplot as plt
import time

from numba import njit, prange
from scipy.sparse import lil_matrix, diags
from scipy.sparse.linalg import eigsh


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


# External potential
def compute_external_potential(X, Y, atom_pos, Z):

    V = np.zeros_like(X)

    for (x0, y0) in atom_pos:
        r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-10
        V += Z / (4.0 * r)

    return V


# Sparse Laplacian
def create_laplacian_sparse(Nx, Ny, dx, dy):

    N = Nx * Ny
    L = lil_matrix((N, N))

    def idx(i, j):
        return (i % Nx) + (j % Ny) * Nx

    for j in range(Ny):
        for i in range(Nx):

            center = idx(i, j)

            L[center, center] = -2.0 / dx**2 - 2.0 / dy**2
            L[center, idx(i-1, j)] = 1.0 / dx**2
            L[center, idx(i+1, j)] = 1.0 / dx**2
            L[center, idx(i, j-1)] = 1.0 / dy**2
            L[center, idx(i, j+1)] = 1.0 / dy**2

    return L.tocsr()


# Numba optimized Hartree potential
@njit(parallel=True)
def compute_hartree_numba(rho, X, Y, dx, dy, epsilon):

    Nx, Ny = rho.shape
    V_H = np.zeros((Nx, Ny))

    for i in prange(Nx):
        for j in range(Ny):

            rx = X[i, j]
            ry = Y[i, j]

            value = 0.0

            for p in range(Nx):
                for q in range(Ny):

                    dxp = X[p, q] - rx
                    dyp = Y[p, q] - ry

                    r = np.sqrt(dxp*dxp + dyp*dyp + epsilon*epsilon)

                    value += rho[p, q] / r

            V_H[i, j] = value * dx * dy

    return V_H


if __name__ == "__main__":

    start_total = time.time()

    V_ext = compute_external_potential(X, Y, atom_pos, Z)

    print("Creating sparse Laplacian...")
    L = create_laplacian_sparse(Nx, Ny, dx, dy)

    max_iter = 2
    num_states = 6
    energy_list = []

    # Initial Hamiltonian
    V_flat_init = V_ext.flatten()
    H_init = -0.5 * L + diags(V_flat_init)

    eigvals_init, eigvecs_init = eigsh(H_init, k=num_states, which='SA')

    psi_init = eigvecs_init.reshape((Nx, Ny, num_states))
    rho = np.sum(np.abs(psi_init)**2, axis=2)

    tol = 1e-3

    for it in range(max_iter):

        print(f"\n--- SCF Iteration {it+1} ---")

        # Hartree potential
        start_h = time.time()
        V_H = compute_hartree_numba(rho, X, Y, dx, dy, 1e-4)
        end_h = time.time()

        # Effective potential
        V_eff = V_ext + V_H
        V_flat = V_eff.flatten()

        # Hamiltonian
        start_ham = time.time()
        H = -0.5 * L + diags(V_flat)
        end_ham = time.time()

        # Eigenvalue solver
        start_eig = time.time()
        eigvals, eigvecs = eigsh(H, k=num_states, which='SA')
        end_eig = time.time()

        psi = eigvecs.reshape((Nx, Ny, num_states))

        rho_new = np.sum(np.abs(psi)**2, axis=2)

        alpha = 0.3
        rho = alpha * rho_new + (1 - alpha) * rho

        total_energy = np.sum(eigvals)
        energy_list.append(total_energy)

        print(f"Energy = {total_energy:.6f}")

        print("Timings (s):")
        print(f"  Hartree Potential: {end_h - start_h:.4f}")
        print(f"  Hamiltonian Construction: {end_ham - start_ham:.4f}")
        print(f"  Eigenvalue Solution: {end_eig - start_eig:.4f}")

        if it > 0:
            delta_E = abs(energy_list[-1] - energy_list[-2])
            if delta_E < tol:
                print("SCF converged.")
                break

    end_total = time.time()

    print(f"\nTotal runtime (Numba version): {end_total - start_total:.4f} s")


    # Visualization
    plt.figure(figsize=(6,5))
    plt.contourf(X, Y, rho, levels=50, cmap='plasma')
    plt.colorbar(label='electron density')
    plt.title("Electron Density after SCF (Numba)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()



# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day9> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day9/DFT_numba.py"
# Creating sparse Laplacian...

# --- SCF Iteration 1 ---
# Energy = 4.355522
# Timings (s):
#   Hartree Potential: 1.4516
#   Hamiltonian Construction: 0.0017
#   Eigenvalue Solution: 0.3497

# --- SCF Iteration 2 ---
# Energy = 4.537730
# Timings (s):
#   Hartree Potential: 0.0839
#   Hamiltonian Construction: 0.0011
#   Eigenvalue Solution: 0.3843

# Total runtime (Numba version): 2.6483 s