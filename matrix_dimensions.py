import random
import numpy as np

def get_matrix_dimensions(matrix):
    num_rows, num_columns = matrix.shape
    return num_rows, num_columns

# example
example_matrix = np.array([[1, 2, 3, 33], [4, 5, 6, 66], [7, 8, 9, 99]])
print(example_matrix)

A = np.array([[2, 0, 0, 1], [0, -1, 2, 1], [2, 1, 0, 3]])
B = np.array([[2, 0], [0, -1], [2, 1]])
C = np.array([[2, 0, 0, 1], [0, -1, 2, 1], [0, -1, 2, 1], [2, 1, 0, 3], [2, 0, 0, 1]])

dimensions = get_matrix_dimensions(example_matrix)

print(f"Matrix dimensions = {dimensions[0]} * {dimensions[1]}")

def generate_matrix(rows, columns, low_limit, high_limit):
    random_matrix = np.random.randint(low_limit, high_limit, size=(rows, columns))
    return random_matrix

print(generate_matrix(3,4, 0, 9))