import ctypes
import os
import time
import numpy as np

# -----------------------------
# 1. Set up paths and load DLL
# -----------------------------
# Make sure sum_parallel.dll is in the same folder as this Python script
dll_path = os.path.abspath("sum_parallel.dll")  # convert to absolute path

# Add MinGW DLL directory for OpenMP runtime (required on Windows)
# Make sure this path matches your MSYS2/MinGW installation
os.add_dll_directory(r"C:/msys64/mingw64/bin")

# Load the DLL
try:
    lib = ctypes.CDLL(dll_path)
except OSError as e:
    print(f"Error loading DLL: {e}")
    print("Check that sum_parallel.dll exists in the script folder and MinGW path is correct.")
    exit(1)

# -----------------------------
# 2. Define argument and return types
# -----------------------------
lib.sum_parallel.argtypes = [ctypes.c_int]
lib.sum_parallel.restype = ctypes.c_longlong  # use long long to handle large sums

# -----------------------------
# 3. Wrapper function
# -----------------------------
def sum_parallel(N):
    return lib.sum_parallel(N)

# -----------------------------
# 4. Small test (N=10,000)
# -----------------------------
N_small = 10_000
print("----- Small Test -----")

start = time.time()
c_sum_small = sum_parallel(N_small)
end = time.time()
print(f"OpenMP C sum (N={N_small}) = {c_sum_small}, Time: {end - start:.6f}s")

start = time.time()
np_sum_small = np.sum(np.arange(1, N_small + 1))
end = time.time()
print(f"NumPy sum (N={N_small}) = {np_sum_small}, Time: {end - start:.6f}s\n")

# -----------------------------
# 5. Large test (N=10,000,000)
# -----------------------------
N_large = 10_000_000
print("----- Large Test -----")

start = time.time()
c_sum_large = sum_parallel(N_large)
end = time.time()
print(f"OpenMP C sum (N={N_large}) = {c_sum_large}, Time: {end - start:.6f}s")

start = time.time()
np_sum_large = np.sum(np.arange(1, N_large + 1))
end = time.time()
print(f"NumPy sum (N={N_large}) = {np_sum_large}, Time: {end - start:.6f}s\n")




# ###Output###
# ----- Small Test -----
# OpenMP C sum (N=10000) = 50005000, Time: 0.001085s
# NumPy sum (N=10000) = 50005000, Time: 0.000102s

# ----- Large Test -----
# OpenMP C sum (N=10000000) = 50000005000000, Time: 0.000591s
# NumPy sum (N=10000000) = 50000005000000, Time: 0.028933s

# #####Observations#####
# - OpenMP C sum is parallelized and usually faster than NumPy for large N.
# - Always use 'long long' in C to avoid integer overflow.
# - For small N, both OpenMP and NumPy give similar results.
# - Make sure sum_parallel.dll and MinGW DLLs are correctly located for Windows.

# 4. Why is the result of OpenMP and NumPy not necessarily the same? How can you fix it?
#    OpenMP and NumPy may differ because the C function originally used int, which can overflow for large sums.
#    Fix: Use long long in C and set ctypes.c_longlong in Python to handle large values safely.