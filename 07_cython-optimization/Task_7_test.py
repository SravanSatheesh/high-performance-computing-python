import time
import numpy as np
import matplotlib.pyplot as plt
from Task_7_laplace_python import laplace_python
from Task_7_laplace_cython import laplace_cython

grid_sizes = [100, 200, 500]

# Create 2x2 subplots with constrained layout
fig, axes = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)
axes = axes.flatten()  # flatten for easy indexing

plot_idx = 0

for N in grid_sizes:
    print(f"Grid size: {N}x{N}")

    # --- Python version (only for N=100) ---
    if N == 100:
        start = time.perf_counter()
        u_py = laplace_python(N)
        python_time = time.perf_counter() - start
        print(f"Python time: {python_time:.4f} s")

        # Plot Python
        ax = axes[plot_idx]
        im = ax.imshow(u_py, cmap="hot", origin="lower")
        ax.set_title(f"Python N={N}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        plot_idx += 1
    else:
        u_py = None
        python_time = None
        print("Python time: Skipped (too slow)")

    # --- Cython version ---
    start = time.perf_counter()
    u_cy = laplace_cython(N)
    cython_time = time.perf_counter() - start
    print(f"Cython time: {cython_time:.4f} s")

    # Plot Cython
    ax = axes[plot_idx]
    im = ax.imshow(u_cy, cmap="hot", origin="lower")
    ax.set_title(f"Cython N={N}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plot_idx += 1

    # Speedup and correctness check
    if python_time is not None:
        speedup = python_time / cython_time
        print(f"Speedup: {speedup:.1f}x")
        close = np.allclose(u_py, u_cy, atol=1e-5)
        max_diff = np.max(np.abs(u_py - u_cy))
        print(f"Results close?: {close}")
        print(f"Max difference: {max_diff:.6f}")
    else:
        print("Speedup: N/A")
    print("-" * 50)

# Add single colorbar for all subplots
fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.6, orientation="vertical")
plt.suptitle("2D Laplace Equation - Python & Cython Solutions", fontsize=16)
plt.show()

# Python version was run for the small grid (100×100) to check correctness and measure runtime. For larger grids (200×200 and 500×500)
# Python runtime would be extremely long, so only Cython was used. This demonstrates the significant speedup achieved by Cython for larger problems

###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_7_test.py
# Grid size: 100x100
# Python time: 56.5079 s
# Cython time: 0.0792 s
# Speedup: 713.1x
# Results close?: True
# Max difference: 0.000000
# --------------------------------------------------
# Grid size: 200x200
# Python time: Skipped (too slow)
# Cython time: 0.3002 s
# Speedup: N/A
# --------------------------------------------------
# Grid size: 500x500
# Python time: Skipped (too slow)
# Cython time: 1.8234 s
# Speedup: N/A
# --------------------------------------------------