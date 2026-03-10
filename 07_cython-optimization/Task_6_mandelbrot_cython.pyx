# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

import numpy as np
cimport numpy as np

cpdef np.ndarray mandelbrot_cython(int width, int height, int max_iter=1000):
    cdef int i, j, k
    cdef double x_min = -2.0
    cdef double x_max = 1.0
    cdef double y_min = -1.5
    cdef double y_max = 1.5

    cdef double real, imag
    cdef double z_real, z_imag
    cdef double z_real2, z_imag2

    # result array
    cdef np.ndarray[np.int32_t, ndim=2] result = np.zeros((height, width), dtype=np.int32)

    for i in range(height):
        imag = y_min + (y_max - y_min) * i / height
        for j in range(width):
            real = x_min + (x_max - x_min) * j / width

            z_real = 0.0
            z_imag = 0.0

            for k in range(max_iter):
                # compute squares FIRST (very important!)
                z_real2 = z_real * z_real
                z_imag2 = z_imag * z_imag

                if z_real2 + z_imag2 > 4.0:
                    break

                # Mandelbrot update (correct order)
                z_imag = 2.0 * z_real * z_imag + imag
                z_real = z_real2 - z_imag2 + real

            result[i, j] = k

    return result