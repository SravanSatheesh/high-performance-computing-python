import sys
import time
import math
import multiprocessing as mp

sys.set_int_max_str_digits(1000000)


def calculate_factorial(n):
    """Sequential factorial."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def partial_product(start, end):
    """Compute product of a sub-range."""
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def parallel_factorial(n, num_processes=None):
    """Parallel factorial using multiprocessing."""
    if num_processes is None:
        num_processes = mp.cpu_count()

    chunk_size = n // num_processes
    ranges = []

    start = 1
    for i in range(num_processes):
        end = start + chunk_size - 1
        if i == num_processes - 1:
            end = n  # last chunk takes the remainder
        ranges.append((start, end))
        start = end + 1

    with mp.Pool(processes=num_processes) as pool:
        partial_results = pool.starmap(partial_product, ranges)

    # combine partial products
    result = 1
    for pr in partial_results:
        result *= pr

    return result


if __name__ == "__main__":
    N = 100000

    # ------------------
    # Sequential
    # ------------------
    start_time = time.time()
    result_sequential = calculate_factorial(N)
    seq_time = time.time() - start_time

    print("sequential result (number of digits):", len(str(result_sequential)))
    print(f"sequential execution time: {seq_time:.2f} seconds")

    # ------------------
    # Parallel
    # ------------------
    start_time = time.time()
    result_parallel = parallel_factorial(N)
    par_time = time.time() - start_time

    print("parallel result (number of digits):", len(str(result_parallel)))
    print(f"parallel execution time: {par_time:.2f} seconds")
