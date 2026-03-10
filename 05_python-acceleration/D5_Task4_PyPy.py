import time
import sys

sys.setrecursionlimit(20000)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


start_time = time.perf_counter()
a = factorial(10000)
end_time = time.perf_counter()
print(f"run time: {end_time - start_time:.10f} seconds")