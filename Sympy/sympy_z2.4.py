import sympy as s

n = s.symbols('n')
prod = 1
n = 2
func = 1 - 1 / pow(n, 2)
while ((1/pow(n,2)) > 0.000001): #В данном случае вычитает крайне малое число
    prod = prod * func
    n = n + 1
    func = 1 - 1 / pow(n, 2)
print(prod)

prod = 1
n = 2
func = 1 - 1 / pow(n, 2)
print('Считает долго. Подождите, пожалуйста.')
while (abs(func) < 1): #В данном случае аналогично, начинает умножаться на 1
    prod = prod * func
    n = n + 1
    func = 1 - 1 / pow(n, 2)
print(prod)

#Приведены два варианта, отличаются ~0.1 
