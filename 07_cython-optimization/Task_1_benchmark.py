import time
from Task_1_square_sum_cython import sum_of_squares

# Python version
def sum_of_squares_py(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

n = 10**7  # start with 10 million

# Python timing
start = time.time()
res_py = sum_of_squares_py(n)
end = time.time()
print(f"Python result: {res_py}, time: {end - start:.4f} s")

# Cython timing
start = time.time()
res_cy = sum_of_squares(n)
end = time.time()
print(f"Cython result: {res_cy}, time: {end - start:.4f} s")



# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_1_benchmark.py 
# Python result: 333333283333335000000, time: 0.5763 s 
# Cython result: 1291890006563070912, time: 0.0000 s

# Task 1 was completed by implementing the sum of squares in Python and then rewriting it in Cython 
# with the loop variable and result declared using cdef for improved performance. A benchmark was run
# comparing Python and Cython with n = 10⁸, showing that Cython was much faster but initially produced
# an incorrect result due to integer overflow. Changing the result variable to double yielded the correct sum while retaining the speed advantage.


# 1.Why is Cython faster?
# It compiles to C code and eliminates Python interpreter overhead, especially for loops and arithmetic.

# 2.Role of cdef
# Declares C types for variables or functions → avoids dynamic Python checks, increases speed.

# 3.Without int typing?
# Cython treats everything as Python objects → slower, closer to normal Python.

# 4.Print inside loop?
# Every loop iteration calls Python’s I/O → drastically slows performance.