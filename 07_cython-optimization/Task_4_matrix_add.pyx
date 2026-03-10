# Task_4_matrix_add.pyx
# cython: boundscheck=False
# cython: wraparound=False

cpdef void add_matrices(double[:, :] A, double[:, :] B, double[:, :] C):
    cdef Py_ssize_t i, j
    cdef Py_ssize_t rows = A.shape[0]
    cdef Py_ssize_t cols = A.shape[1]
    
    for i in range(rows):
        for j in range(cols):
            C[i, j] = A[i, j] + B[i, j]