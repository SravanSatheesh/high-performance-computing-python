import numpy as np

# 1. Create an array with 20 random real numbers between -1 and 1
arr = np.random.uniform(-1, 1, 20)
print("Original array:\n", arr)

# 2. Find all positive values
positive_values = arr[arr > 0]
print("Positive values:\n", positive_values)

# 3. Set all negative values to 0
arr[arr < 0] = 0
print("Negative values set to 0:\n", arr)

# 4. Replace all values between 0.2 and 0.5 with their square
arr[(arr >= 0.2) & (arr <= 0.5)] = arr[(arr >= 0.2) & (arr <= 0.5)] ** 2
print("Values between 0.2 and 0.5 squared:\n", arr)

# ###Output###
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task7.py"
# Original array:
#  [ 0.55296255  0.54005046 -0.54147975 -0.51297849 -0.44429143  0.35893128
#  -0.96964354 -0.47347826 -0.8952491  -0.71144948  0.80546973 -0.82541927
#  -0.88238156  0.12091998 -0.1729085   0.37709462 -0.51368254  0.08393465
#   0.54079831 -0.15721885]
# Positive values:
#  [0.55296255 0.54005046 0.35893128 0.80546973 0.12091998 0.37709462
#  0.08393465 0.54079831]
# Negative values set to 0:
#  [0.55296255 0.54005046 0.         0.         0.         0.35893128
#  0.         0.         0.         0.         0.80546973 0.
#  0.         0.12091998 0.         0.37709462 0.         0.08393465
#  0.54079831 0.        ]
# Values between 0.2 and 0.5 squared:
#  [0.55296255 0.54005046 0.         0.         0.         0.12883166
#  0.         0.         0.         0.         0.80546973 0.
#  0.         0.12091998 0.         0.14220035 0.         0.08393465
#  0.54079831 0.        ]