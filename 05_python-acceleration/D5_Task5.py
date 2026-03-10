import time
import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only check divisors up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):  # check only odd divisors
        if n % i == 0:
            return False
    return True


def count_primes(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count


if __name__ == "__main__":

    # Loop over different input sizes
    test_values = [100_000, 500_000]

    for n in test_values:
        start = time.perf_counter()
        result = count_primes(n)
        end = time.perf_counter()

        print(f"\nNumber of primes below {n}: {result}")
        print(f"Runtime: {end - start:.6f} seconds")

