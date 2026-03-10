# Task_5_mat_mul.pyx
# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np
from libc.stdlib cimport malloc, free

# --- Standard matrix multiplication ---
cpdef void mat_mul(double[:, :] A, double[:, :] B, double[:, :] C):
    cdef Py_ssize_t i, j, k
    cdef Py_ssize_t n = A.shape[0]
    cdef Py_ssize_t m = A.shape[1]
    cdef Py_ssize_t p = B.shape[1]
    
    for i in range(n):
        for j in range(p):
            C[i, j] = 0.0
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]

# --- Element-wise multiplication ---
cpdef void elementwise_mul(double[:, :] A, double[:, :] B, double[:, :] C):
    cdef Py_ssize_t i, j
    cdef Py_ssize_t rows = A.shape[0]
    cdef Py_ssize_t cols = A.shape[1]
    
    for i in range(rows):
        for j in range(cols):
            C[i, j] = A[i, j] * B[i, j]

# --- Scaled matrix addition: C = alpha*A + beta*B ---
cpdef void scaled_add(double[:, :] A, double[:, :] B, double[:, :] C, double alpha, double beta):
    cdef Py_ssize_t i, j
    cdef Py_ssize_t rows = A.shape[0]
    cdef Py_ssize_t cols = A.shape[1]
    
    for i in range(rows):
        for j in range(cols):
            C[i, j] = alpha * A[i, j] + beta * B[i, j]