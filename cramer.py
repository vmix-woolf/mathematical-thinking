import numpy as np

def solve_cramer(a, b, verbose=False):
    ma, mb = np.copy(a), np.copy(b)
    n = len(mb)
    det_a = round(np.linalg.det(ma))

    if det_a == 0:
        return None  # system is not solving

    x = np.zeros(n)
    for i in range(n):
        ai = ma.copy()
        ai[:, i] = mb
        x[i] = round(np.linalg.det(ai) / det_a)

    return x

A = np.array([
  [-1, 1, 2],
  [0, -1, -3],
  [4, -3, 2]
])
B = np.array([
  1, -4, 7
])

print(f"Вектор рішення: \r\n {solve_cramer(A, B)}")