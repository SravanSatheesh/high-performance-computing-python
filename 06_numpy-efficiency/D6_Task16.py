import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import time

# -----------------------------
# 1. Original list-based Mandelbrot
# -----------------------------
def mandelbrot(z, maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

def mandelbrot_list(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    result = []
    for r in r1:
        for i in r2:
            result.append(mandelbrot(complex(r, i), maxiter))
    result = np.reshape(result, (width, height))
    return r1, r2, result

# -----------------------------
# 2. NumPy loop version
# -----------------------------
def mandelbrot_numpy_loop(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    result = np.zeros((width, height), dtype=np.int32)
    for ix, r in enumerate(r1):
        for iy, i in enumerate(r2):
            result[ix, iy] = mandelbrot(complex(r, i), maxiter)
    return r1, r2, result

# -----------------------------
# 3. Fully vectorized NumPy version
# -----------------------------
def mandelbrot_numpy(c, maxiter):
    output = np.zeros(c.shape, dtype=np.int32)
    z = np.zeros(c.shape, dtype=np.complex64)
    for it in range(maxiter):
        mask = np.abs(z) <= 2
        output[mask] = it
        z[mask] = z[mask] * z[mask] + c[mask]
    output[output == maxiter - 1] = 0
    return output

# -----------------------------
# 4. Parameters
# -----------------------------
xmin, xmax = -2.0, 0.5
ymin, ymax = -1.25, 1.25
width, height = 500, 500
maxiter = 80

# -----------------------------
# 5. Runtime comparison
# -----------------------------
start = time.time()
r1, r2, res_list = mandelbrot_list(xmin, xmax, ymin, ymax, width, height, maxiter)
print("List version runtime: {:.4f} s".format(time.time() - start))

start = time.time()
r1, r2, res_loop = mandelbrot_numpy_loop(xmin, xmax, ymin, ymax, width, height, maxiter)
print("NumPy loop version runtime: {:.4f} s".format(time.time() - start))

# Vectorized
X, Y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))
C = X + 1j*Y
start = time.time()
res_vec = mandelbrot_numpy(C, maxiter)
print("Vectorized NumPy version runtime: {:.4f} s".format(time.time() - start))

# -----------------------------
# 6. Visualization of vectorized Mandelbrot
# -----------------------------
plt.figure(figsize=(8,8))
plt.imshow(res_vec.T, cmap='plasma', origin='lower')
plt.title("Vectorized NumPy Mandelbrot Set")
plt.colorbar(label='Iteration count')
plt.show()

# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task16.py"
# List version runtime: 1.3972 s
# NumPy loop version runtime: 1.2810 s
# Vectorized NumPy version runtime: 0.2093 s

# 1. Mathematical expression repeatedly calculated:
#    z = z^2 + c

# 2. X-axis and Y-axis:
#    X-axis: Real part of complex plane
#    Y-axis: Imaginary part of complex plane

# 3. Pixel color meaning:
#    Number of iterations before |z| > 2 (escape speed)

# 6. Computation times:
#    List version: slowest
#    NumPy loop version: faster
#    Vectorized NumPy version: fastest

# 7. Reason for speed difference:
#    Vectorized NumPy avoids Python loop overhead and uses optimized C code internally

# 8. Runtime scaling at higher resolution:
#    Increases with number of pixels; vectorized version scales much better than loops

# 9. Best color map for visualization:
#    'plasma', 'inferno', or 'magma' show Mandelbrot structure clearly

# 10. Image quality:
#     Low resolution: blocky, less detail
#     High resolution: fine details of fractal visible

# 11. Memory requirement:
#     Increases with higher resolution; a 4000x4000 array uses significantly more RAM

# 12. Data types to save memory:
#     np.uint8 or np.int16 can reduce memory usage compared to np.int32