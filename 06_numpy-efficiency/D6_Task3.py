#Task 3.1
import time
import numpy as np

# 10 million numbers
size = 10_000_000
data = np.linspace(0, 2*np.pi, size)

# Using Python loop
start = time.time()
result_loop = [np.sin(x) for x in data]
end = time.time()
print('Task3.1')
print(f"Runtime with Python loop: {end - start:.5f} seconds")

# Using NumPy vectorization
start = time.time()
result_vec = np.sin(data)
end = time.time()
print(f"Runtime with NumPy vectorization: {end - start:.5f} seconds")

#Task3.2
import numpy as np

# Create 5x5 random matrix between 0 and 10
A = np.random.rand(5, 5) * 10
print('Task3.2')
print("Original matrix:\n", A)

# Subtract column mean using broadcasting
A_centered = A - A.mean(axis=0)
print("Matrix after subtracting column means:\n", A_centered)

# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task3.py"
# Task3.1
# Runtime with Python loop: 3.01968 seconds
# Runtime with NumPy vectorization: 0.08604 seconds
# Task3.2
# Original matrix:
#  [[1.43889876 8.93879984 7.71149006 4.39502073 2.31374861]
#  [1.95210368 6.04506226 3.57357483 1.02568658 1.81848012]
#  [2.50109798 3.16807864 2.23862496 5.04446376 4.01285413]
#  [0.20512868 5.84454305 9.96152671 8.34832993 2.39566347]
#  [2.55626407 1.86401662 4.49469087 4.75348646 0.18607951]]
# Matrix after subtracting column means:
#  [[-0.29179987  3.76669976  2.11550857 -0.31837676  0.16838344]
#  [ 0.22140505  0.87296218 -2.02240665 -3.68771091 -0.32688505]
#  [ 0.77039934 -2.00402144 -3.35735653  0.33106627  1.86748896]
#  [-1.52556995  0.67244297  4.36554523  3.63493244  0.2502983 ]
#  [ 0.82556544 -3.30808347 -1.10129061  0.04008897 -1.95928566]]

# 3.1 Calculating sine values of 10 million numbers is significantly faster with NumPy vectorization compared to a Python loop because vectorized operations avoid explicit iteration and leverage optimized C routines.
# 3.2 Broadcasting allows subtracting the mean of each column from the entire column without using loops, making the operation concise and efficient.