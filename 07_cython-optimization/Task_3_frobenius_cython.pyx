# Task_3_frobenius_cython.pyx
# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np

def euclidean_norm(np.ndarray[np.float64_t, ndim=2] matrix):
    cdef Py_ssize_t i, j
    cdef double total = 0.0
    cdef Py_ssize_t rows = matrix.shape[0]
    cdef Py_ssize_t cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            total += matrix[i, j] * matrix[i, j]
    return total ** 0.5