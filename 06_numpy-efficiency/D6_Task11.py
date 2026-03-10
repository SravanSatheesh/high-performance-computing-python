import numpy as np

# Create a list of 100 integers
arr = np.arange(100)
print("Original array:", arr)

# Shuffle the array randomly (in-place)
np.random.shuffle(arr)
print("Shuffled array:", arr)

# Draw a random sample of 10 values without replacement
sample_without_replacement = np.random.choice(arr, size=10, replace=False)
print("Sample without replacement:", sample_without_replacement)

# Draw a random sample of 10 values with replacement
sample_with_replacement = np.random.choice(arr, size=10, replace=True)
print("Sample with replacement:", sample_with_replacement)

# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task11.py"
# Original array: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#  48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
#  72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
#  96 97 98 99]
# Shuffled array: [37 91 66 76 65 99  7  9  2 82  0 85 87 67 20 49 78 29 57 53 92  8 46 44
#   5 73 31 98 68 26 42 86 81 23 69 62 74 33 34 30 72 24 93 38 61 32 15 60
#   3 97 36 41 19 64 59 45  1 83 88  4 18 27 17 50 94 51 75 25 12 95 21 14
#  89 96 28 43 22 47 54 56 48 80 84 58 13  6 71 70 10 11 63 55 39 35 40 52
#  90 79 16 77]
# Sample without replacement: [39 52 81 64 42 32 71 56 82 66]
# Sample with replacement: [82 15 32 97 38 71 71 29 92 59]