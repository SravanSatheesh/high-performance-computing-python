import cProfile
import pstats

# -----------------------------------
# Step 1: Profile the code
# -----------------------------------
profiler = cProfile.Profile()

# Start profiling
profiler.enable()

# Run your code directly
exec(open("extension.py").read())

# Stop profiling
profiler.disable()

# -----------------------------------
# Step 2: Save profiling data to "results.prof"
# -----------------------------------
stats = pstats.Stats(profiler)
stats.dump_stats("results.prof")
print("Profiling data saved as 'results.prof'.")

# -----------------------------------
# Step 3: Optional inspection
# -----------------------------------
stats.strip_dirs()
stats.sort_stats('cumulative')

print("\n=== Top 10 functions by cumulative time ===")
stats.print_stats(10)