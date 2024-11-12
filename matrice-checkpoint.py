import numpy as np

def print_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])


    if rows != cols:
        print("Матриця не є квадратною. Головна та побічна діагоналі не визначені.")
        return


    main_diagonal = [matrix[i][i] for i in range(rows)]
    anti_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]


    print("Головна діагональ:", main_diagonal)
    print("Побічна діагональ:", anti_diagonal)


# Приклад використання
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_diagonals(matrix_example)

matrix1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print(matrix1)

# Створення одиничної матриці розміром 4x4
identity_matrix = np.eye(4)
print(identity_matrix)
