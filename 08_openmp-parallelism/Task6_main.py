import ctypes
import os
import time
import numpy as np

# -----------------------------
# 1. Load shared library
# -----------------------------
dll_path = os.path.abspath("histogram.dll")
os.add_dll_directory(r"C:/msys64/mingw64/bin")
lib = ctypes.CDLL(dll_path)

# -----------------------------
# 2. Define function signatures
# -----------------------------
lib.compute_histogram_incorrect.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.uint8, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lib.compute_histogram_incorrect.restype = None

lib.compute_histogram_atomic.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.uint8, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lib.compute_histogram_atomic.restype = None

lib.compute_histogram_reduction.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.uint8, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lib.compute_histogram_reduction.restype = None

# -----------------------------
# 3. Generate random data
# -----------------------------
size = 10_000_000
data = np.random.randint(0, 256, size=size, dtype=np.uint8)

# -----------------------------
# 4. Incorrect version
# -----------------------------
hist_incorrect = np.zeros(256, dtype=np.int32)
start = time.perf_counter()
lib.compute_histogram_incorrect(data, hist_incorrect, size)
end = time.perf_counter()
print(f"Incorrect C histogram time: {end - start:.6f} s")

# -----------------------------
# 5. Atomic version
# -----------------------------
hist_atomic = np.zeros(256, dtype=np.int32)
start = time.perf_counter()
lib.compute_histogram_atomic(data, hist_atomic, size)
end = time.perf_counter()
print(f"Atomic C histogram time: {end - start:.6f} s")

# -----------------------------
# 6. Reduction version
# -----------------------------
hist_reduction = np.zeros(256, dtype=np.int32)
start = time.perf_counter()
lib.compute_histogram_reduction(data, hist_reduction, size)
end = time.perf_counter()
print(f"Reduction C histogram time: {end - start:.6f} s")

# -----------------------------
# 7. NumPy reference
# -----------------------------
start = time.perf_counter()
hist_np = np.bincount(data, minlength=256)
end = time.perf_counter()
print(f"NumPy histogram time: {end - start:.6f} s")

# -----------------------------
# 8. Compare results
# -----------------------------
diff_incorrect = np.max(np.abs(hist_incorrect - hist_np))
diff_atomic = np.max(np.abs(hist_atomic - hist_np))
diff_reduction = np.max(np.abs(hist_reduction - hist_np))

print(f"Max difference (Incorrect vs NumPy): {diff_incorrect}")
print(f"Max difference (Atomic vs NumPy): {diff_atomic}")
print(f"Max difference (Reduction vs NumPy): {diff_reduction}")



# ###Outptu###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day8> python Task6_main.py
# Incorrect C histogram time: 0.044495 s
# Atomic C histogram time: 0.062918 s
# Reduction C histogram time: 0.001717 s
# NumPy histogram time: 0.042229 s
# Max difference (Incorrect vs NumPy): 13704
# Max difference (Atomic vs NumPy): 0
# Max difference (Reduction vs NumPy): 0


# ###Comprehension Answers###

# 1. Why do race conditions occur during histogram calculation?
# Race conditions happen because multiple threads try to update the same histogram bin at the same time. Since the increment operation (histogram[value]++) is not atomic by default, some increments can be lost, producing incorrect results.

# 2. When is #pragma omp critical necessary, and when is #pragma omp atomic sufficient?
# #pragma omp atomic is sufficient when only a single, simple operation (like incrementing a counter) needs to be performed safely.
# #pragma omp critical is necessary when more complex operations need exclusive access, such as updating multiple elements, performing conditional checks, or merging arrays.

# 3. Which method performs better for this task and why?
# The reduction approach (per-thread local histograms) performs best.
# Reason: Each thread works independently most of the time, avoiding synchronization overhead. Only a single merge happens at the end, making it much faster than atomic or critical-based methods.

# 4. What alternatives are there to synchronization (e.g., local histograms)?
# Using thread-local histograms (one per thread) and then merging them at the end.
# Using partitioning of data so that each thread writes to a separate memory region.
# These methods avoid frequent contention on shared memory.

# 5. What other OpenMP synchronization methods do you know?
# #pragma omp barrier → wait until all threads reach the barrier.
# #pragma omp flush → ensures memory consistency across threads.
# #pragma omp ordered → preserves sequential order in loops.
# Locks (omp_lock_t) → manual lock/unlock for critical sections.
# Reduction clauses (reduction(+:var)) → automatic per-thread reduction.