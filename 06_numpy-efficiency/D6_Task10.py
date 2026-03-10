import numpy as np

# Original array
a = np.arange(10)
print("Original array a:", a)

# Create a view
b = a[2:7]
b[0] = 99
print("After modifying view b[0]:")
print("Array a:", a)  # a is affected because b is a view

# Create a copy
c = a[2:7].copy()
c[0] = 77
print("After modifying copy c[0]:")
print("Array a:", a)  # a is NOT affected because c is a copy


# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task10.py"
# Original array a: [0 1 2 3 4 5 6 7 8 9]
# After modifying view b[0]:
# Array a: [ 0  1 99  3  4  5  6  7  8  9]
# After modifying copy c[0]:
# Array a: [ 0  1 99  3  4  5  6  7  8  9]

# When modifying the view b, the original array a changes because b shares the same memory as a.
# When modifying the copy c, the original array a remains unchanged because c has its own separate memory.