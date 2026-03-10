import numpy as np
import matplotlib.pyplot as plt
import time

from dft_cython import compute_hartree_cython  # compiled Cython function

# Grid parameters
Nx, Ny = 60, 60
Lx, Ly = 20.0, 20.0
dx, dy = Lx/Nx, Ly/Ny
x = np.linspace(-Lx/2, Lx/2, Nx)
y = np.linspace(-Ly/2, Ly/2, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')

# Atom positions
atom_pos = [(-3.33, 0.0), (3.33, 0.0)]
Z = 6

# External potential
def compute_external_potential(X,Y):
    V = np.zeros_like(X)
    for (x0,y0) in atom_pos:
        r = np.sqrt((X-x0)**2 + (Y-y0)**2) + 1e-10
        V += Z/(4*r)
    return V

# Laplacian (dense, small grid for example)
def create_laplacian():
    N = Nx*Ny
    L = np.zeros((N,N))
    def idx(i,j): return i + j*Nx
    for j in range(Ny):
        for i in range(Nx):
            c = idx(i,j)
            L[c,c] = -2/dx**2 - 2/dy**2
            if i>0: L[c,idx(i-1,j)] = 1/dx**2
            if i<Nx-1: L[c,idx(i+1,j)] = 1/dx**2
            if j>0: L[c,idx(i,j-1)] = 1/dy**2
            if j<Ny-1: L[c,idx(i,j+1)] = 1/dy**2
    return L

# SCF loop
V_ext = compute_external_potential(X,Y)
L = create_laplacian()
rho = np.ones((Nx,Ny))*0.1
num_states = 4
max_iter = 2
tol = 1e-3
energy_list = []

for it in range(max_iter):
    print(f"\n--- SCF Iteration {it+1} ---")
    start_h = time.time()
    V_H = compute_hartree_cython(rho, X, Y, dx, dy)
    end_h = time.time()

    V_eff = V_ext + V_H
    V_flat = V_eff.flatten()
    H = -0.5*L + np.diag(V_flat)

    start_eig = time.time()
    eigvals, eigvecs = np.linalg.eigh(H)
    end_eig = time.time()

    psi = eigvecs[:,:num_states].reshape((Nx,Ny,num_states))
    rho_new = np.sum(np.abs(psi)**2, axis=2)
    alpha = 0.3
    rho = alpha*rho_new + (1-alpha)*rho

    total_energy = np.sum(eigvals[:num_states])
    energy_list.append(total_energy)

    print(f"Energy = {total_energy:.6f}")
    print(f"Hartree time: {end_h-start_h:.4f}s, Eigenvalue: {end_eig-start_eig:.4f}s")

# Plot
plt.contourf(X,Y,rho,levels=40)
plt.colorbar(label="Electron Density")
plt.show()


# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day9> python DFT_Cython.py        

# --- SCF Iteration 1 ---
# Energy = 466.123033
# Hartree time: 0.0773s, Eigenvalue: 8.5450s

# --- SCF Iteration 2 ---
# Energy = 329.022793
# Hartree time: 0.0650s, Eigenvalue: 8.5003s