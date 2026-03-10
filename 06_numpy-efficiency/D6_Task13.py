import numpy as np

# 1. Create a 3D array with dimensions (2, 3, 4)
arr3d = np.random.rand(2, 3, 4)

# 2. Mean value along each axis
mean_axis0 = arr3d.mean(axis=0)  # Shape: (3, 4)
mean_axis1 = arr3d.mean(axis=1)  # Shape: (2, 4)
mean_axis2 = arr3d.mean(axis=2)  # Shape: (2, 3)

print("Mean along axis 0:\n", mean_axis0)
print("Mean along axis 1:\n", mean_axis1)
print("Mean along axis 2:\n", mean_axis2)

# 3. Convert the 3D array into a 2D array
arr2d = arr3d.reshape(2, 12)  # Flatten last two dimensions
print("Reshaped 2D array (2,12):\n", arr2d)

# 4. Transpose the array
arr_transposed = arr2d.T  # Swap rows and columns
print("Transposed 2D array (12,2):\n", arr_transposed)
# Explanation: Transposing flips the shape so rows become columns and columns become rows.


# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task13.py"
# Mean along axis 0:
#  [[0.33607683 0.48566817 0.64513269 0.21952047]
#  [0.13086529 0.78256503 0.85736552 0.11859435]
#  [0.57520429 0.60359975 0.31832138 0.17274793]]
# Mean along axis 1:
#  [[0.38679208 0.66998958 0.57784712 0.19103385]
#  [0.30797219 0.57789905 0.63603261 0.14954132]]
# Mean along axis 2:
#  [[0.43807035 0.52492324 0.40625338]
#  [0.40512873 0.41977185 0.4286833 ]]
# Reshaped 2D array (2,12):
#  [[0.6061084  0.22917924 0.83862177 0.07837199 0.05889869 0.95693015
#   0.86803127 0.21583286 0.49536915 0.82385937 0.02688831 0.27889669]
#  [0.06604526 0.7421571  0.4516436  0.36066895 0.20283189 0.60819992
#   0.84669978 0.02135583 0.65503942 0.38334014 0.60975445 0.06659918]]
# Transposed 2D array (12,2):
#  [[0.6061084  0.06604526]
#  [0.22917924 0.7421571 ]
#  [0.83862177 0.4516436 ]
#  [0.07837199 0.36066895]
#  [0.05889869 0.20283189]
#  [0.95693015 0.60819992]
#  [0.86803127 0.84669978]
#  [0.21583286 0.02135583]
#  [0.49536915 0.65503942]
#  [0.82385937 0.38334014]
#  [0.02688831 0.60975445]
#  [0.27889669 0.06659918]]