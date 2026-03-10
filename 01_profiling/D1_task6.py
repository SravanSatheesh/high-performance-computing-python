import time
import cProfile
import pstats


# 1. Factorial function
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. Generate square values
def do_stuff():
    result = []
    for i in range(1000000):
        result.append(i * i)
    return result


# 3. Waste time
def waste_time():
    time.sleep(5)
    print("Finished wasting time!")


# 4. Main function
def main():
    print("Calculating factorial of 10...")
    print(fact(10))

    print("Generating square values...")
    do_stuff()

    print("Wasting some time...")
    waste_time()


# 5. Profiling, sorting, filtering, saving, and reloading
if __name__ == "__main__":

    # Create profiler object
    profiler = cProfile.Profile()

    # Start profiling
    profiler.enable()
    main()
    profiler.disable()

    # Create Stats object from profiler
    stats = pstats.Stats(profiler)

    # Remove unnecessary path information
    stats.strip_dirs()

    # ---------------------------------------
    # A) Sort by cumulative time
    # ---------------------------------------
    print("\n=== Sorted by cumulative time ===")
    stats.sort_stats("cumulative")
    stats.print_stats(10)  # Show top 10 functions

    # ---------------------------------------
    # B) Filter by function name
    # ---------------------------------------
    print("\n=== Filter: do_stuff ===")
    stats.print_stats("do_stuff")

    # ---------------------------------------
    # C) Save profiling data externally
    # ---------------------------------------
    stats.dump_stats("profiling_results.prof")
    print("\nProfile data saved as 'profiling_results.prof'")

    # ---------------------------------------
    # D) Reload saved profile data
    # ---------------------------------------
    print("\n=== Reloading saved profile data ===")
    loaded_stats = pstats.Stats("profiling_results.prof")
    loaded_stats.strip_dirs()
    loaded_stats.sort_stats("cumulative")
    loaded_stats.print_stats(10)