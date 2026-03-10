import time
import matplotlib.pyplot as plt
import numpy as np
from Task_6_mandelbrot_cython import mandelbrot_cython
from Task_6_mandelbrot_python import mandelbrot_python

width, height = 1000, 1000

# --- Python ---
start = time.perf_counter()
mandelbrot_py = mandelbrot_python(width, height)
python_time = time.perf_counter() - start
print(f"Python Mandelbrot time: {python_time:.5f} s")

# --- Cython ---
start = time.perf_counter()
mandelbrot_cy = mandelbrot_cython(width, height)
cython_time = time.perf_counter() - start
print(f"Cython Mandelbrot time: {cython_time:.5f} s")

# Compare correctness with tolerance
print("Results equal (with tolerance)?",
      np.allclose(mandelbrot_py, mandelbrot_cy))

# --- Plot Cython version ---
plt.imshow(mandelbrot_cy, cmap="hot", extent=(-2,1,-1.5,1.5))
plt.colorbar()
plt.title("Mandelbrot Set - Cython")
plt.show()


# ###Outptu###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day7> python Task_6_test.py
# Python Mandelbrot time: 25.53513 s
# Cython Mandelbrot time: 0.57649 s
# Results equal (with tolerance)? True