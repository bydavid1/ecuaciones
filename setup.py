from sistemas_ecuaciones import gauss_elimination

a = [[2, 1], [5, 7]]
b = [11, 13]
x = gauss_elimination(a, b)
print(x)