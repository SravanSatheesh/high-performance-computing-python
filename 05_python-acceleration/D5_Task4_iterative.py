import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    start_time = time.perf_counter()
    a = factorial_iterative(10000)
    end_time = time.perf_counter()
    print(f"Iterative run time: {end_time - start_time:.10f} seconds")