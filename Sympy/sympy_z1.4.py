import sympy as s

n = s.symbols('n')
func = s.factorial(n)*s.exp(n)/pow(n,n)/s.sqrt(n)
lim = s.limit(func, n, s.oo)
print(lim)

