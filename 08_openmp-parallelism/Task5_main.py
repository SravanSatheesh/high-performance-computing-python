import ctypes
import os
import time
import numpy as np

# -----------------------------
# 1. Load shared library
# -----------------------------
dll_path = os.path.abspath("matvec_parallel.dll")  # Windows DLL
os.add_dll_directory(r"C:/msys64/mingw64/bin")     # MinGW DLLs for OpenMP
lib = ctypes.CDLL(dll_path)

# -----------------------------
# 2. Define function signature
# -----------------------------
lib.matvec_parallel.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lib.matvec_parallel.restype = None

# -----------------------------
# 3. Wrapper function
# -----------------------------
def matvec_parallel(A, x):
    N = A.shape[0]
    y = np.zeros(N, dtype=np.double)
    lib.matvec_parallel(A, x, y, N)
    return y

# -----------------------------
# 4. Performance test
# -----------------------------
N = 500  # Adjust to 500–1000 depending on RAM

# Random matrix and vector
A = np.random.rand(N, N).astype(np.double)
x = np.random.rand(N).astype(np.double)

# -----------------------------
# 5. OpenMP C version
# -----------------------------
start = time.perf_counter()
y_c = matvec_parallel(A, x)
end = time.perf_counter()
print(f"OpenMP C matvec time: {end - start:.6f} s")

# -----------------------------
# 6. NumPy version
# -----------------------------
start = time.perf_counter()
y_np = A @ x
end = time.perf_counter()
print(f"NumPy matvec time: {end - start:.6f} s")

# -----------------------------
# 7. Verify correctness
# -----------------------------
max_diff = np.max(np.abs(y_c - y_np))
print(f"Maximum difference between OpenMP C and NumPy: {max_diff:e}")

# ###Outptu###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day8> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8/Task5_main.py"
# OpenMP C matvec time: 0.001105 s
# NumPy matvec time: 0.000256 s
# Maximum difference between OpenMP C and NumPy: 3.126388e-13

# Comprehension Answers

# 1. Why does it make sense to parallelize the outer loop in a matrix-vector multiplication?
# The outer loop iterates over rows of the matrix, and each row computation is independent.
# Parallelizing the outer loop allows multiple threads to compute different rows simultaneously without interfering with each other, giving efficient workload distribution.

# 2. What problems can arise when multiple threads write to the same memory areas?
# If multiple threads try to write to the same variable or array element, it can cause race conditions, leading to incorrect results.
# In matrix-vector multiplication, this is avoided because each thread writes to a distinct element of the output vector.

# 3. How does the speedup behave for small vs. large matrices?
# For small matrices, OpenMP overhead (thread creation and management) can make the parallel version slower than optimized NumPy.
# For large matrices, the computation dominates the overhead, and OpenMP achieves noticeable speedup over serial implementations.

# 4. What role does memory access (cache, memory layout) play in performance?
# Matrices stored in row-major order are accessed more efficiently if loops follow this layout.
# Poor memory access (non-contiguous reads) can cause cache misses, slowing down performance even if parallelized.

# 5. Why is double better than float for large N?
# double provides higher precision and reduces rounding errors, which is important when summing or multiplying many numbers.
# For large matrices, float may accumulate significant errors, while double maintains numerical stability