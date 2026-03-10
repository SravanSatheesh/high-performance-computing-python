import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit

# 1. Initialization

N = 1000
alpha = 0.01


u_initial = np.zeros(N)
u_initial[N // 2] = 100.0  # Temperature shock in the center


# 2. Simulation without Numba

def simulate_heat_plain(u, steps, alpha):
    u = u.copy()
    for t in range(steps):
        u_new = u.copy()
        for i in range(1, len(u) - 1):
            u_new[i] = u[i] + alpha * (u[i - 1] - 2 * u[i] + u[i + 1])
        u = u_new
    return u

# 3. Simulation with Numba

@jit(nopython=True)
def simulate_heat_numba(u, steps, alpha):
    u = u.copy()
    for t in range(steps):
        u_new = u.copy()
        for i in range(1, len(u) - 1):
            u_new[i] = u[i] + alpha * (u[i - 1] - 2 * u[i] + u[i + 1])
        u = u_new
    return u



# 4. Measure execution time for different step sizes

step_values = [1000, 5000, 10000]

for s in step_values:
    print("\n==============================")
    print("Number of steps:", s)

    # Plain Python
    start = time.time()
    u_plain = simulate_heat_plain(u_initial, s, alpha)
    end = time.time()
    print("Plain Python Time:", end - start, "seconds")

    # Numba first run (compile included only once overall)
    start = time.time()
    u_numba = simulate_heat_numba(u_initial, s, alpha)
    end = time.time()
    print("Numba Run Time:", end - start, "seconds")

# 5. Visualization
plt.figure(figsize=(10, 5))
plt.plot(u_initial, label="Initial Temperature")
plt.plot(u_plain, label="After Simulation (Plain)")
plt.plot(u_numba, linestyle="--", label="After Simulation (Numba)")
plt.legend()
plt.title("1D Heat Conduction Simulation")
plt.xlabel("Position")
plt.ylabel("Temperature")
plt.show()