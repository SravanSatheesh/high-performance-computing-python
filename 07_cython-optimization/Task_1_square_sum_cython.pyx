def sum_of_squares(int n):
    cdef int i
    cdef double result = 0.0  # double avoids overflow
    for i in range(n):
        result += i * i
    return result