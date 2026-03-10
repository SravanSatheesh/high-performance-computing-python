import numpy as np
import time
import matplotlib.pyplot as plt

def mandelbrot_python(width, height, max_iter=1000):
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5

    result = np.zeros((height, width), dtype=np.int32)

    for i in range(height):
        imag = y_min + (y_max - y_min) * i / height
        for j in range(width):
            real = x_min + (x_max - x_min) * j / width

            z_real = 0.0
            z_imag = 0.0

            for k in range(max_iter):
                z_real2 = z_real * z_real
                z_imag2 = z_imag * z_imag

                if z_real2 + z_imag2 > 4.0:
                    break

                z_imag = 2.0 * z_real * z_imag + imag
                z_real = z_real2 - z_imag2 + real

            result[i, j] = k

    return result


# Benchmark
width, height = 1000, 1000
start = time.perf_counter()
mandelbrot_py = mandelbrot_python(width, height)
python_time = time.perf_counter() - start
print(f"Python Mandelbrot time: {python_time:.5f} s")

# Plot
plt.imshow(mandelbrot_py, cmap="hot", extent=(-2,1,-1.5,1.5))
plt.colorbar()
plt.title("Mandelbrot Set - Python")
plt.show()