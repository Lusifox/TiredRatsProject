import numpy as np

a = np.array([11, 1, 44, 3, 66, 10, 0, 55])

r = np.linalg.norm(a, ord = np.inf)

print('Норма вектора:', r)