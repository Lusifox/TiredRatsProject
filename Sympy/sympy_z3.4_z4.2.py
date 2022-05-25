from sympy import *
from sympy.abc import x


res=diff(x**x)
print(res)


print()

res=integrate(x*x*sin(x))
print(res)
