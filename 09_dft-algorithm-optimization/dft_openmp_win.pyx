# cython: boundscheck=False, wraparound=False, cdivision=True
from cython.parallel cimport prange
cimport cython
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
def compute_V_H(double[:,:] X, double[:,:] Y, double[:,:] rho,
                double[:,:] V_H, double dx, double dy, double epsilon) nogil:

    cdef int Nx = X.shape[0]
    cdef int Ny = X.shape[1]
    cdef int i, j, p, q
    cdef double rx, ry, dxp, dyp, r, value

    # Outer loop parallelized with OpenMP
    for i in prange(Nx, schedule='static', nogil=True):
        for j in range(Ny):
            value = 0.0
            rx = X[i,j]
            ry = Y[i,j]
            for p in range(Nx):
                for q in range(Ny):
                    dxp = X[p,q] - rx
                    dyp = Y[p,q] - ry
                    r = sqrt(dxp*dxp + dyp*dyp + epsilon*epsilon)
                    value += rho[p,q] / r
            V_H[i,j] = value * dx * dy