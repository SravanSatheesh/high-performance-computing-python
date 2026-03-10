import time
import squares


def sum_of_squares_python(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


if __name__ == "__main__":
    n = int(input("Enter n: "))
    # Fortran version

    start = time.perf_counter()
    result_fortran = squares.squares_module.sum_of_squares(n)
    end = time.perf_counter()
    print("\nFortran result:", result_fortran)
    print("Fortran runtime:", end - start, "seconds")


    # Python version

    start = time.perf_counter()
    result_python = sum_of_squares_python(n)
    end = time.perf_counter()
    print("\nPython result:", result_python)
    print("Python runtime:", end - start, "seconds")

    # Check correctness
    print("\nResults equal:", result_fortran == result_python)