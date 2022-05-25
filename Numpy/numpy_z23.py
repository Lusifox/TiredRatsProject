from numpy import *

n=int(input("n="))
x=array([i for i in range(1,n+1)])
print(x)

print()

print("произведение элементов = ",nanprod(x))
print()
print("стандартное отклонение = ",nanstd(x))
print()
print("Индекс минимального значения = ",nanargmin(x))
