from cython.parallel import prange
cimport cython
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def laplace_cython(int N, int max_iter=5000):
    cdef np.ndarray[np.float64_t, ndim=2] u = np.zeros((N, N), dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=2] u_new = np.zeros((N, N), dtype=np.float64)
    cdef int i, j, iter_count

    # Boundary conditions
    for j in range(N):
        u[0, j] = 100.0
        u_new[0, j] = 100.0

    cdef double diff
    for iter_count in range(max_iter):
        diff = 0.0
        with nogil:
            for i in prange(1, N-1, schedule='static'):
                for j in range(1, N-1):
                    u_new[i, j] = 0.25*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])
        u, u_new = u_new, u

    return u