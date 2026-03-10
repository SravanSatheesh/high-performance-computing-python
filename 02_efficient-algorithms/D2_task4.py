import cProfile
import pstats
from Task_4 import generate_signal, detect_anomalies_time, detect_anomalies_fft

sizes = [10_000, 100_000, 1_000_000]


def profile_function(func, signal):
    profiler = cProfile.Profile()
    profiler.enable()
    func(signal)
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("tottime")   # sort by internal execution time
    stats.print_stats(10)         # show top 10 time-consuming calls


for n in sizes:
    print(f"\n==============================")
    print(f"Signal size: {n}")
    print(f"==============================")

    signal = generate_signal(n)

    print("\n--- Time-Domain Detection ---")
    profile_function(detect_anomalies_time, signal)

    print("\n--- FFT-Based Detection ---")
    profile_function(detect_anomalies_fft, signal)