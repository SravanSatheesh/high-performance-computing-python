import time
import numpy as np
from Task_2_sum_array_python import sum_array as sum_py
from Task_2_sum_array_cython import sum_array as sum_cy

arr = np.arange(1, 10**7, dtype=np.float64)

# Python benchmark
start = time.time()
res_py = sum_py(arr)
end = time.time()
print(f"Python result: {res_py}, time: {end - start:.4f} s")

# Cython benchmark
start = time.time()
res_cy = sum_cy(arr)
end = time.time()
print(f"Cython result: {res_cy}, time: {end - start:.4f} s")


# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_2_benchmark.py   
# Python result: 49999995000000.0, time: 1.3003 s
# Cython result: 49999995000000.0, time: 0.0112 s


# 1. Why is the Cython version faster?
# The Cython version runs faster because it compiles the code into C, uses 
# variables with fixed types, and accesses arrays directly through memoryviews.
# This avoids Python’s dynamic typing and interpreted loops, allowing the sum
# to be calculated much more efficiently.

# 2. What role does cdef play?
# cdef declares C-level variables and types. By specifying the type of the loop 
# index and the sum, Cython generates optimized machine code and eliminates the 
# overhead of Python objects, improving performance.

# 3. What happens if you insert print(i) inside the loop?
# Printing inside the loop dramatically slows execution because Python has to 
# process a print operation for each iteration. This cancels out the performance
# benefit of Cython.

# 4. What do the decorators @boundscheck(False) and @wraparound(False) do?
# @boundscheck(False) disables checks that array indices are within valid bounds,
# and @wraparound(False) disables negative index wraparound. Both speed up array
# access in loops, but the programmer must ensure that indices are correct to avoid errors.