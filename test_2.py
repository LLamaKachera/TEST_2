##testeando codigo de minimizacion de costos
from scipy.optimize import linprog

# Coeficientes de la función objetivo (costos por kg de maíz, residuo en grasa, alfalfa)
c = [42, 36, 30]

# Coeficientes de las restricciones (carbohidratos, proteínas, vitaminas)
A = [
    [-90, -20, -40],  # Carbohidratos
    [-30, -80, -60],  # Proteínas
    [-10, -20, -60]   # Vitaminas
]

# Requerimientos nutricionales mínimos (valores negativos para cumplir con >=)
b = [-200, -180, -150]

# Restricciones de no negatividad (x1, x2, x3 >= 0)
x_bounds = (0, None)

# Resolver el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds, x_bounds], method='highs')

# Resultados
res.x, res.fun
