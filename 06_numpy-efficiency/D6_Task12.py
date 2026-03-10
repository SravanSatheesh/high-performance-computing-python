import numpy as np

# 1. Create an array with 50 values between -5 and 5
arr = np.linspace(-5, 5, 50)

# 2. Positive AND > 2
mask_pos_gt2 = (arr > 0) & (arr > 2)
arr[mask_pos_gt2] = np.abs(arr[mask_pos_gt2])

# 3. Negative OR < -3
mask_neg_lt3 = (arr < 0) | (arr < -3)
arr[mask_neg_lt3] = np.abs(arr[mask_neg_lt3])

# 4. Either < 0 or between 3 and 4
mask_lt0_or_3_4 = (arr < 0) | ((arr >= 3) & (arr <= 4))
arr[mask_lt0_or_3_4] = np.abs(arr[mask_lt0_or_3_4])

# 5. Show the final array
print("Final array after masking and replacing with absolute values:\n", arr)


# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day6/D6_Task12.py"
# Final array after masking and replacing with absolute values:
#  [5.         4.79591837 4.59183673 4.3877551  4.18367347 3.97959184
#  3.7755102  3.57142857 3.36734694 3.16326531 2.95918367 2.75510204
#  2.55102041 2.34693878 2.14285714 1.93877551 1.73469388 1.53061224
#  1.32653061 1.12244898 0.91836735 0.71428571 0.51020408 0.30612245
#  0.10204082 0.10204082 0.30612245 0.51020408 0.71428571 0.91836735
#  1.12244898 1.32653061 1.53061224 1.73469388 1.93877551 2.14285714
#  2.34693878 2.55102041 2.75510204 2.95918367 3.16326531 3.36734694
#  3.57142857 3.7755102  3.97959184 4.18367347 4.3877551  4.59183673
#  4.79591837 5.        ]