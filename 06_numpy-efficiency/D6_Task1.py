import numpy as np

# ===============================
# Task 1.1: Create different NumPy arrays
# ===============================

# 1D array from 10 to 50 with step size 5
array_1d = np.arange(10, 51, 5)
print("1D array (10 to 50 step 5):")
print(array_1d)

# 3x3 matrix of ones
ones_matrix = np.ones((3, 3))
print("\n3x3 matrix of ones:")
print(ones_matrix)

# 5x5 identity matrix
identity_matrix = np.eye(5)
print("\n5x5 identity matrix:")
print(identity_matrix)

# 10x10 matrix with random numbers between 0 and 1
random_matrix = np.random.rand(10, 10)
print("\n10x10 random matrix:")
print(random_matrix)


# ===============================
# Task 1.2: Array manipulation
# ===============================

# Create 3x3 array with numbers 1 to 9
array_3x3 = np.arange(1, 10).reshape(3, 3)
print("\n3x3 array (1 to 9):")
print(array_3x3)

# Extract first row
first_row = array_3x3[0, :]
print("\nFirst row:")
print(first_row)

# Extract middle column
middle_column = array_3x3[:, 1]
print("\nMiddle column:")
print(middle_column)

# Reshape into 1x9 matrix
reshaped_array = array_3x3.reshape(1, 9)
print("\nReshaped to 1x9:")
print(reshaped_array)


# ###Output###
# --------------
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task1.py"
# 1D array (10 to 50 step 5):
# [10 15 20 25 30 35 40 45 50]

# 3x3 matrix of ones:
# [[1. 1. 1.]        
#  [1. 1. 1.]        
#  [1. 1. 1.]]       

# 5x5 identity matrix:
# [[1. 0. 0. 0. 0.]  
#  [0. 1. 0. 0. 0.]  
#  [0. 0. 1. 0. 0.]  
#  [0. 0. 0. 1. 0.]  
#  [0. 0. 0. 0. 1.]] 

# 10x10 random matrix:
# [[0.30180365 0.34496613 0.55235395 0.02589363 0.23167685 0.29834193
#   0.99554106 0.30200565 0.31474246 0.53996945]
#  [0.94642011 0.28186441 0.70017098 0.56835829 0.79674696 0.99342648
#   0.48718952 0.29331096 0.57027025 0.31818462]
#  [0.82889858 0.47574076 0.18506379 0.06210663 0.65949169 0.04398333
#   0.9041455  0.38415043 0.43246761 0.51898649]
#  [0.62914047 0.19765216 0.50078178 0.35504788 0.27528522 0.22756722
#   0.13971271 0.06769573 0.09301996 0.44069168]
#  [0.43025651 0.75549465 0.68341609 0.87042305 0.7118794  0.24593438
#   0.15730394 0.8491319  0.35911642 0.956209  ]
#  [0.74417802 0.04964347 0.93438011 0.18717825 0.40137286 0.20913853
#   0.90598799 0.84367021 0.4991047  0.05635967]
#  [0.23471618 0.03188825 0.13224446 0.44101849 0.11472905 0.36602886
#   0.8714862  0.51385468 0.73557374 0.04110007]
#  [0.32201518 0.01992968 0.34101619 0.43618387 0.69699192 0.94139778
#   0.34839165 0.95038177 0.85236506 0.89489266]
#  [0.96382557 0.22457329 0.10190373 0.14929906 0.59668994 0.01379802
#   0.68202959 0.03351455 0.66611744 0.47481378]
#  [0.98842484 0.90597396 0.62304412 0.69084661 0.15719055 0.24502097
#   0.39165306 0.18466463 0.21050985 0.670271  ]]

# 3x3 array (1 to 9):
#  [4 5 6]
#  [7 8 9]]

# First row:
# [1 2 3]

# Middle column:
# [2 5 8]

# Reshaped to 1x9:
# [[1 2 3 4 5 6 7 8 9]]
