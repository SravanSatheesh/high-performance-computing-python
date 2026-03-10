import numpy as np
import time
from Task_4_matrix_add import add_matrices

def benchmark_matrix_addition(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.zeros((size, size))

    # --- Cython ---
    # Using time.perf_counter()
    start_perf = time.perf_counter()
    add_matrices(A, B, C)
    cython_perf = time.perf_counter() - start_perf

    # Using time.time()
    start_time = time.time()
    add_matrices(A, B, C)
    cython_time = time.time() - start_time

    # --- NumPy ---
    start_perf = time.perf_counter()
    C_np = A + B
    numpy_perf = time.perf_counter() - start_perf

    start_time = time.time()
    C_np = A + B
    numpy_time = time.time() - start_time

    # --- Pure Python loops ---
    C_py = np.zeros((size, size))

    start_perf = time.perf_counter()
    for i in range(size):
        for j in range(size):
            C_py[i, j] = A[i, j] + B[i, j]
    python_perf = time.perf_counter() - start_perf

    start_time = time.time()
    for i in range(size):
        for j in range(size):
            C_py[i, j] = A[i, j] + B[i, j]
    python_time = time.time() - start_time

    # --- Print results ---
    print(f"Matrix size: {size}x{size}")
    print(f"Cython: perf_counter={cython_perf:.5f}s, time={cython_time:.5f}s")
    print(f"NumPy:  perf_counter={numpy_perf:.5f}s, time={numpy_time:.5f}s")
    print(f"Python: perf_counter={python_perf:.5f}s, time={python_time:.5f}s")
    print("-" * 50)

# Run benchmarks for different sizes
for sz in [100, 500, 1000]:
    benchmark_matrix_addition(sz)

####Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_4_matrix_add_test.py
# Matrix size: 100x100
# Cython: perf_counter=0.00006s, time=0.00000s
# NumPy:  perf_counter=0.00006s, time=0.00000s
# Python: perf_counter=0.00329s, time=0.00000s
# --------------------------------------------------
# Matrix size: 500x500
# Cython: perf_counter=0.00069s, time=0.00000s
# NumPy:  perf_counter=0.00048s, time=0.00000s
# Python: perf_counter=0.08688s, time=0.08536s
# --------------------------------------------------
# Matrix size: 1000x1000
# Cython: perf_counter=0.00321s, time=0.00200s
# NumPy:  perf_counter=0.00232s, time=0.00200s
# Python: perf_counter=0.35182s, time=0.35110s
# --------------------------------------------------