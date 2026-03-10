# dft_cython.pyx

import numpy as np
cimport numpy as np
from libc.math cimport sqrt

# Hartree potential optimized with Cython
def compute_hartree_cython(np.ndarray[np.double_t, ndim=2] rho,
                           np.ndarray[np.double_t, ndim=2] X,
                           np.ndarray[np.double_t, ndim=2] Y,
                           double dx, double dy,
                           double epsilon=1e-4):

    cdef int Nx = rho.shape[0]
    cdef int Ny = rho.shape[1]
    cdef np.ndarray[np.double_t, ndim=2] V_H = np.zeros((Nx, Ny), dtype=np.double)

    cdef int i, j, p, q
    cdef double rx, ry, dxp, dyp, r, value

    for i in range(Nx):
        for j in range(Ny):
            rx = X[i,j]
            ry = Y[i,j]
            value = 0.0
            for p in range(Nx):
                for q in range(Ny):
                    dxp = X[p,q] - rx
                    dyp = Y[p,q] - ry
                    r = sqrt(dxp*dxp + dyp*dyp + epsilon*epsilon)
                    value += rho[p,q] / r
            V_H[i,j] = value * dx * dy

    return V_H