import time
import numpy as np

# Number of elements
N = 10_000_000

print("=== Using Python Lists ===")

# Create lists
list_a = list(range(N))
list_b = list(range(N))

# Addition
start = time.time()
list_add = [x + y for x, y in zip(list_a, list_b)]
end = time.time()
print("List addition time:", end - start, "seconds")

# Multiplication
start = time.time()
list_mul = [x * y for x, y in zip(list_a, list_b)]
end = time.time()
print("List multiplication time:", end - start, "seconds")

# Squaring
start = time.time()
list_square = [x ** 2 for x in list_a]
end = time.time()
print("List squaring time:", end - start, "seconds")


print("\n=== Using NumPy Arrays ===")

# Create NumPy arrays
arr_a = np.arange(N)
arr_b = np.arange(N)

# Addition
start = time.time()
arr_add = arr_a + arr_b
end = time.time()
print("NumPy addition time:", end - start, "seconds")

# Multiplication
start = time.time()
arr_mul = arr_a * arr_b
end = time.time()
print("NumPy multiplication time:", end - start, "seconds")

# Squaring
start = time.time()
arr_square = arr_a ** 2
end = time.time()
print("NumPy squaring time:", end - start, "seconds")

# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task2.py"
# === Using Python Lists ===
# List addition time: 0.9331824779510498 seconds
# List multiplication time: 1.3861103057861328 seconds
# List squaring time: 1.4011452198028564 seconds

# === Using NumPy Arrays ===
# NumPy addition time: 0.04605245590209961 seconds
# NumPy multiplication time: 0.07438111305236816 seconds
# NumPy squaring time: 0.05521249771118164 seconds
# -----------------------------------------------------

# . NumPy operations are significantly faster than Python lists because NumPy uses vectorized 
#   operations implemented in optimized C code, while Python lists rely on slower Python-level loops.