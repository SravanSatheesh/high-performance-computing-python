import numpy as np
import matplotlib.pyplot as plt

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

# External Potential (Coulomb-like)
def compute_external_potential(X, Y, atom_pos, Z):
    V = np.zeros_like(X)
    for (x0, y0) in atom_pos:
        r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-10
        V += Z / (4.0 * r)
    return V

# Laplace-Operator
def create_laplacian(Nx, Ny, dx, dy):
    N = Nx * Ny
    L = np.zeros((N, N))

    def idx(i, j):
        #Mapping of 2D-Gitterkoordinaten onto 1D-Index
        return (i % Nx) + (j % Ny) * Nx

    for j in range(Ny):
        for i in range(Nx):
            center = idx(i, j)

            # center cell
            L[center, center] = -2.0 / dx**2 - 2.0 / dy**2

            # neighboring cell left (i-1, j)
            L[center, idx(i - 1, j)] = 1.0 / dx**2

            # neighboring cell right (i+1, j)
            L[center, idx(i + 1, j)] = 1.0 / dx**2

            # neighboring cell below (i, j-1)
            L[center, idx(i, j - 1)] = 1.0 / dy**2

            # neighboring cell above (i, j+1)
            L[center, idx(i, j + 1)] = 1.0 / dy**2

    return L

# Hartree-Potential in real space
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


# SCF-loop
V_ext = compute_external_potential(X, Y, atom_pos, Z)
L = create_laplacian(Nx, Ny, dx, dy)

max_iter = 2
num_states = 6
energy_list = []



# Starting value for density
# Beginning Hamiltonians only with external potential
V_flat_init = V_ext.flatten()
H_init = -0.5 * L + np.diag(V_flat_init)

# Calculate eigenstates
eigvals_init, eigvecs_init = np.linalg.eigh(H_init)
eigvecs_init = eigvecs_init[:, :num_states]

# Reshape wave functions and calculate density
psi_init = eigvecs_init.reshape((Nx, Ny, num_states))
rho = np.sum(np.abs(psi_init)**2, axis=2)




tol = 1e-3


for it in range(max_iter):
    # Hartree-Potential in real space
    V_H = compute_hartree_potential(rho, dx, dy)

    # Effective Potential
    V_eff = V_ext + V_H
    V_flat = V_eff.flatten()

    # Hamiltonian: H = -0.5 * Laplace + V_eff as diagonal matrix
    H = -0.5 * L + np.diag(V_flat)

    # Calculate all eigenvalues/ eigenfunctions
    eigvals_all, eigvecs_all = np.linalg.eigh(H)

    # Extract smallest num_states states
    eigvals = eigvals_all[:num_states]
    eigvecs = eigvecs_all[:, :num_states]

    # Reshaping wave functions
    psi = eigvecs.reshape((Nx, Ny, num_states))

    # Calculate electron density (sum the squares of the magnitudes)
    rho_new = np.sum(np.abs(psi)**2, axis=2)

    # Attenuation of density
    alpha = 0.3
    rho = alpha * rho_new + (1 - alpha) * rho

    # save energy value
    total_energy = np.sum(eigvals)
    energy_list.append(total_energy)

    print(f"Iteration {it+1:2d}: Energy = {total_energy:.6f}")

    if it > 0:
        delta_E = np.abs(energy_list[-1] - energy_list[-2])
        if delta_E < tol:
            print(f"Convergence achieved after {it+1} iterations (ΔE = {delta_E:.6f})")
            break

# Visualization of the converged electron density
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, rho, levels=50, cmap='plasma')
plt.colorbar(label='electron density $\\rho(r)$')
plt.title('Converged electron density after SCF')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()
