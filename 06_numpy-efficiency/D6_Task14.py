import numpy as np

# 1. Create a 4x4 matrix with random values
A = np.random.rand(4, 4)
print("Matrix A:\n", A)

# 2. Calculate the determinant
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# 3. Calculate the inverse
A_inv = np.linalg.inv(A)
print("Inverse of A:\n", A_inv)

# 4. Verify A * A_inv ≈ I
identity_check = np.dot(A, A_inv)
print("A multiplied by A_inv:\n", identity_check)


# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task14.py"
# Matrix A:
#  [[0.36069095 0.33557917 0.31378488 0.48636958]
#  [0.38857778 0.64218856 0.67559039 0.97173377]
#  [0.74459444 0.75639685 0.94912718 0.49084047]
#  [0.50757773 0.66864863 0.52022387 0.81985134]]
# Determinant of A: -0.013854760706575757
# Inverse of A:
#  [[ 6.9156246  -2.41406742  0.16729566 -1.34150426]
#  [-9.57699772 -2.1132631   0.27309726  8.02272547]
#  [ 0.56830949  2.84848118  1.30008277 -4.49167652]
#  [ 3.16860033  1.4106331  -1.15125231 -1.6427239 ]]
# A multiplied by A_inv:
#  [[ 1.00000000e+00 -4.31943560e-17 -1.07686014e-16 -6.48367600e-16]
#  [ 1.47128975e-16  1.00000000e+00 -1.16347862e-16 -6.83290236e-16]
#  [-3.17427118e-16 -1.20506730e-17  1.00000000e+00 -6.27475805e-16]
#  [-9.78005140e-17  1.86775066e-16 -1.98086749e-17  1.00000000e+00]]