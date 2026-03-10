import time
import fibonacci


# Pure Python implementation (recursive)
def fib_python(n):
    if n <= 1:
        return n
    return fib_python(n - 1) + fib_python(n - 2)


if __name__ == "__main__":

    n = 35  

    # --- Fortran version (compiled with f2py) ---
    start = time.perf_counter()
    result_fortran = fibonacci.fibonacci_module.fibonacci(n)
    end = time.perf_counter()

    print(f"Fortran Fibonacci({n}) = {result_fortran}")
    print(f"Fortran runtime: {end - start:.6f} seconds")

    # --- Pure Python version ---
    start = time.perf_counter()
    result_python = fib_python(n)
    end = time.perf_counter()

    print(f"Python Fibonacci({n}) = {result_python}")
    print(f"Python runtime: {end - start:.6f} seconds")