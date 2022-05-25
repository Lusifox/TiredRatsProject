import numpy as np

a = np.array([11, 1, 44, 3, 6, 10, 0, 55])

for i in range(len(a)):
    if a[i]>=0 and a[i]<=10:
        print('Число из диапозона [0, 10]:', a[i])
