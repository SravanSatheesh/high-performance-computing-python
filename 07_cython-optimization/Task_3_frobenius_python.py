import numpy as np

def euclidean_norm(matrix):
    total = 0.0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            total += matrix[i, j] ** 2
    return total ** 0.5

# Example usage
if __name__ == "__main__":
    mat = np.random.rand(1000, 1000)
    print(euclidean_norm(mat))