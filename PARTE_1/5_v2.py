def latas_restantes(m, j):
    s = m - j
    t = (s + 1) * j
    r = m * (m + 1) // 2
    return r - t

# Leer los valores de m y j desde la entrada
m, j = map(int, input().split())

# Calcular y mostrar el número de latas restantes
print(latas_restantes(m, j))
