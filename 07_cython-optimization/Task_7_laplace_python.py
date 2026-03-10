import numpy as np

def laplace_python(N, max_iter=5000, tol=1e-5):
    u = np.zeros((N, N), dtype=np.float64)
    u[0, :] = 100.0  # top boundary

    u_new = u.copy()

    for _ in range(max_iter):
        diff = 0.0
        for i in range(1, N-1):
            for j in range(1, N-1):
                u_new[i, j] = 0.25 * (
                    u[i+1, j] + u[i-1, j] +
                    u[i, j+1] + u[i, j-1]
                )
                diff = max(diff, abs(u_new[i, j] - u[i, j]))
        u, u_new = u_new, u
        if diff < tol:
            break
    return u