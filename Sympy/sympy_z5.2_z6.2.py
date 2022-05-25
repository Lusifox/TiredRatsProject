from sympy import *
from sympy.solvers.solveset import nonlinsolve
from sympy.plotting import plot


#5(2)

x = Symbol('x')
y = Symbol('y')
system = [tan(x**2 - y) - 0.48*(x+y), (x - 0.2)**2 - 3*y**2 - 1.5]
vars = [x, y]
print(nonlinsolve(system, vars))

#№6(2)

p1=plot(x*x*x-x*x-22*x+40, show=False)
p1.show()