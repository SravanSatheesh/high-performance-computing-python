import time
import numpy as np
from Task_3_frobenius_python import euclidean_norm as norm_py
from Task_3_frobenius_cython import euclidean_norm as norm_cy

matrix = np.random.rand(1000, 1000)

# Python benchmark
start = time.time()
res_py = norm_py(matrix)
end = time.time()
print(f"Python result: {res_py}, time: {end - start:.4f} s")

# Cython benchmark
start = time.time()
res_cy = norm_cy(matrix)
end = time.time()
print(f"Cython result: {res_cy}, time: {end - start:.4f} s")


# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_3_benchmark.py
# Python result: 577.6767870901778, time: 0.3240 s
# Cython result: 577.6767870901778, time: 0.0010 s


# 1. What is a memory view in Cython? Why is it faster than a Python array?
# A memory view is a typed, contiguous view of an array (like a NumPy array) that
# allows Cython to access elements directly at C speed. It avoids Python object overhead 
# and supports efficient multi-dimensional indexing.

# 2. When should you use cpdef instead of def or cdef?
# cpdef is used when a function needs to be fast like cdef but also callable from
# Python code. cdef is only callable from Cython, and def is slower because it handles general Python objects dynamically.

# 3. How do Cython functions with and without type specifications differ in runtime?
# Cython functions with type specifications (cdef variables, typed arrays) run much faster because the compiler can generate optimized 
# C code and avoid Python overhead. Untyped functions behave like normal Python functions, so they are slower.