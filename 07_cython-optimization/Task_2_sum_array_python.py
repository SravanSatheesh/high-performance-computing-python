# Task_2_sum_array_python.py
def sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Optional: only run this if the file is executed directly
if __name__ == "__main__":
    import numpy as np
    arr = np.arange(1, 10**7, dtype=np.float64)
    print(sum_array(arr))