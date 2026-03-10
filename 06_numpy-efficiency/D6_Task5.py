import numpy as np

# 1. Integer array (int32)
arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("Integer array (int32):", arr_int32)

# 2. Float array (float64)
arr_float64 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print("\nFloat array (float64):", arr_float64)

# 3. Compare memory consumption
print('\n---Memory Comparison---')
print("Memory usage of int32 array:", arr_int32.nbytes, "bytes")
print("Memory usage of float64 array:", arr_float64.nbytes, "bytes")

# 4. Convert float64 to int16
arr_int16 = arr_float64.astype(np.int16)
print("\nConverted to int16:", arr_int16)
print("Memory used:", arr_int16.nbytes, "bytes")

# ###Output###
# -------------------
# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task5.py"
# Integer array (int32): [1 2 3 4 5]

# Float array (float64): [1. 2. 3. 4. 5.]

# ---Memory Comparison---
# Memory usage of int32 array: 20 bytes
# Memory usage of float64 array: 40 bytes

# Converted to int16: [1 2 3 4 5]
# Memory used: 10 bytes