import time
import cProfile
import pstats


# -------------------------------
# Functions to profile
# -------------------------------

def fact(n):
    """Calculate factorial iteratively."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def do_stuff():
    """Generate squares from 0 to 999999."""
    result = []
    for i in range(1_000_000):
        result.append(i * i)
    return result


def waste_time():
    """Pause execution for 5 seconds."""
    time.sleep(5)
    print("Finished wasting time.")


# -------------------------------
# Main program
# -------------------------------

def main():
    print("Factorial of 5:", fact(5))

    squares = do_stuff()
    print("Generated", len(squares), "square values.")

    waste_time()


# -------------------------------
# Profiling (Task 3 solution)
# -------------------------------

if __name__ == "__main__":

    # Create profiler
    profiler = cProfile.Profile()

    # Start profiling
    profiler.enable()

    # Run program
    main()

    # Stop profiling
    profiler.disable()

    # Create readable statistics
    results = pstats.Stats(profiler)

    # Improve readability
    results.strip_dirs()           # remove long paths
    results.sort_stats("tottime")  # sort by longest runtime

    # Print profiling results
    print("\n--- Profiling Results ---")
    results.print_stats(10)        # top 10 functions