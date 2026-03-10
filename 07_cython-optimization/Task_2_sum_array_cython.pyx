# Task_2_sum_array_cython.pyx
# cython: boundscheck=False
# cython: wraparound=False

def sum_array(double[:] arr):
    cdef Py_ssize_t i
    cdef double total = 0.0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total
    