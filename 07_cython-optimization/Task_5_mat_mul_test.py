import numpy as np
import time
from Task_5_mat_mul import mat_mul, elementwise_mul, scaled_add

# Function to benchmark all three operations
def benchmark_operations(sizes):
    for size in sizes:
        print(f"\n--- Matrix size: {size}x{size} ---")

        # Create random matrices
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        C = np.zeros((size, size))

        # ----------------- Matrix Multiplication -----------------
        # Cython
        start = time.perf_counter()
        mat_mul(A, B, C)
        cython_time = time.perf_counter() - start

        # NumPy
        start = time.perf_counter()
        C_np = A @ B
        numpy_time = time.perf_counter() - start

        # Correctness check
        correct = np.allclose(C, C_np)

        print(f"Matrix multiplication - Correct: {correct}")
        print(f"Cython time: {cython_time:.5f}s, NumPy time: {numpy_time:.5f}s")

        # ----------------- Element-wise Multiplication -----------------
        start = time.perf_counter()
        elementwise_mul(A, B, C)
        cython_elem_time = time.perf_counter() - start
        C_np_elem = A * B
        correct_elem = np.allclose(C, C_np_elem)
        print(f"Element-wise multiplication - Correct: {correct_elem}, Cython time: {cython_elem_time:.5f}s")

        # ----------------- Scaled Matrix Addition -----------------
        alpha, beta = 2.0, 3.0
        start = time.perf_counter()
        scaled_add(A, B, C, alpha, beta)
        cython_scaled_time = time.perf_counter() - start
        C_np_scaled = alpha * A + beta * B
        correct_scaled = np.allclose(C, C_np_scaled)
        print(f"Scaled addition - Correct: {correct_scaled}, Cython time: {cython_scaled_time:.5f}s")

# Run benchmarks for requested sizes
benchmark_operations([500, 1000, 2000])




###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_5_mat_mul_test.py


# --- Matrix size: 500x500 ---
# Matrix multiplication - Correct: True
# Cython time: 0.13516s, NumPy time: 0.00388s
# Element-wise multiplication - Correct: True, Cython time: 0.00076s
# Scaled addition - Correct: True, Cython time: 0.00106s

# --- Matrix size: 1000x1000 ---
# Matrix multiplication - Correct: True
# Cython time: 2.20914s, NumPy time: 0.01475s
# Element-wise multiplication - Correct: True, Cython time: 0.00217s
# Scaled addition - Correct: True, Cython time: 0.00221s

# --- Matrix size: 2000x2000 ---
# Matrix multiplication - Correct: True
# Cython time: 45.34866s, NumPy time: 0.13062s
# Element-wise multiplication - Correct: True, Cython time: 0.00936s
# Scaled addition - Correct: True, Cython time: 0.00937s

#COMPREHENSION QUESTIONS
# 1. Why is NumPy sometimes still faster than your own Cython function?**
# NumPy uses highly optimized, vectorized C/Fortran code, making it faster than simple Cython loops.

# 2. What would happen if you used `nogil` or `prange`?**
# They allow parallel execution by releasing the Python GIL, which speeds up large loops across multiple cores.
