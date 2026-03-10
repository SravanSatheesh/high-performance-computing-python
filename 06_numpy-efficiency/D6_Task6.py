import numpy as np

# 1. Create a 5x5 matrix with values from 0 to 24
matrix = np.arange(25).reshape(5, 5)
print("Original 5x5 matrix:\n", matrix)

# 2. Extract the diagonal
diagonal = np.diag(matrix)
print("Diagonal:", diagonal)

# 3. Extract the upper left 3x3 submatrix
submatrix_3x3 = matrix[:3, :3]
print("Upper left 3x3 submatrix:\n", submatrix_3x3)

# 4. Extract the last column
last_column = matrix[:, -1]
print("Last column:", last_column)

# 5. Extract all odd rows (1st, 3rd, 5th in 0-indexed: 1,3)
odd_rows = matrix[1::2, :]
print("Odd rows:\n", odd_rows)

# 6. Replace all values greater than 10 with 0
matrix_gt10_zeroed = matrix.copy()
matrix_gt10_zeroed[matrix_gt10_zeroed > 10] = 0
print("Matrix with values > 10 replaced by 0:\n", matrix_gt10_zeroed)

# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task6.py"
# Original 5x5 matrix:
#  [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
#  Diagonal: [ 0  6 12 18 24]
# Upper left 3x3 submatrix:
#  [[ 0  1  2]
#  [ 5  6  7]
#  [10 11 12]]
# Last column: [ 4  9 14 19 24]
# Odd rows:
#  [[ 5  6  7  8  9]
#  [15 16 17 18 19]]
# Matrix with values > 10 replaced by 0:
#  [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10  0  0  0  0]
#  [ 0  0  0  0  0]
#  [ 0  0  0  0  0]]