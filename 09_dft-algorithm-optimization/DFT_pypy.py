import numpy as np
import matplotlib.pyplot as plt
import time

# Grid parameters
Nx, Ny = 60, 60   # smaller grid for PyPy dense solver
Lx, Ly = 20.0, 20.0
dx, dy = Lx / Nx, Ly / Ny

x = np.linspace(-Lx/2, Lx/2, Nx)
y = np.linspace(-Ly/2, Ly/2, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

# Atom positions
atom_pos = [(-3.33, 0.0), (3.33, 0.0)]
Z = 6


# External potential
def compute_external_potential(X, Y):

    V = np.zeros_like(X)

    for (x0, y0) in atom_pos:
        for i in range(Nx):
            for j in range(Ny):
                r = np.sqrt((X[i,j]-x0)**2 + (Y[i,j]-y0)**2) + 1e-10
                V[i,j] += Z/(4*r)

    return V


# Hartree potential (loop-heavy → PyPy speeds this up)
def compute_hartree_potential(rho):

    V_H = np.zeros_like(rho)

    for i in range(Nx):
        for j in range(Ny):

            rx = X[i,j]
            ry = Y[i,j]

            value = 0.0

            for p in range(Nx):
                for q in range(Ny):

                    dxp = X[p,q] - rx
                    dyp = Y[p,q] - ry

                    r = np.sqrt(dxp*dxp + dyp*dyp + 1e-4)

                    value += rho[p,q] / r

            V_H[i,j] = value * dx * dy

    return V_H


# Laplacian matrix
def create_laplacian():

    N = Nx * Ny
    L = np.zeros((N,N))

    def idx(i,j):
        return i + j*Nx

    for j in range(Ny):
        for i in range(Nx):

            center = idx(i,j)

            L[center,center] = -2/dx**2 - 2/dy**2

            if i>0:
                L[center,idx(i-1,j)] = 1/dx**2
            if i<Nx-1:
                L[center,idx(i+1,j)] = 1/dx**2
            if j>0:
                L[center,idx(i,j-1)] = 1/dy**2
            if j<Ny-1:
                L[center,idx(i,j+1)] = 1/dy**2

    return L


if __name__ == "__main__":

    start_total = time.time()

    V_ext = compute_external_potential(X,Y)

    print("Creating Laplacian matrix...")
    L = create_laplacian()

    num_states = 4
    max_iter = 2

    rho = np.ones((Nx,Ny))*0.1

    energy_list = []

    for it in range(max_iter):

        print(f"\n--- SCF Iteration {it+1} ---")

        # Hartree potential
        start_h = time.time()
        V_H = compute_hartree_potential(rho)
        end_h = time.time()

        V_eff = V_ext + V_H
        V_flat = V_eff.flatten()

        # Hamiltonian
        start_ham = time.time()
        H = -0.5*L + np.diag(V_flat)
        end_ham = time.time()

        # Eigenvalues
        start_eig = time.time()
        eigvals, eigvecs = np.linalg.eigh(H)
        end_eig = time.time()

        psi = eigvecs[:,:num_states].reshape((Nx,Ny,num_states))

        rho = np.sum(np.abs(psi)**2, axis=2)

        total_energy = np.sum(eigvals[:num_states])
        energy_list.append(total_energy)

        print(f"Energy = {total_energy:.6f}")

        print("Timings (s):")
        print(f"  Hartree Potential: {end_h-start_h:.4f}")
        print(f"  Hamiltonian Construction: {end_ham-start_ham:.4f}")
        print(f"  Eigenvalue Solution: {end_eig-start_eig:.4f}")

    end_total = time.time()

    print(f"\nTotal runtime (PyPy test): {end_total-start_total:.4f} s")


# Plot density
    plt.figure(figsize=(6,5))
    plt.contourf(X,Y,rho,levels=40)
    plt.colorbar(label="Electron Density")
    plt.title("Electron Density (PyPy Test)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day9> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day9/DFT_pypy.py"
# Creating Laplacian matrix...

# --- SCF Iteration 1 ---
# Energy = 26.122577
# Timings (s):
#   Hartree Potential: 13.4184
#   Hamiltonian Construction: 0.1365
#   Eigenvalue Solution: 8.6864

# --- SCF Iteration 2 ---
# Energy = 2.130116
# Timings (s):
#   Hartree Potential: 13.2869
#   Hamiltonian Construction: 0.1102
#   Eigenvalue Solution: 8.1995

# Total runtime (PyPy test): 43.8729 s