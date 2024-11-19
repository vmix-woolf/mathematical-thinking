import numpy as np
import math

from numpy.ma.core import arctan

# Оголошення вихідної матриці
matrix = np.array([[1, 0, 3],
                   [-1, -1, 2],
                   [4, 7, 2]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)
print(matrix.dot(inverse_matrix))

print(arctan(0.25))