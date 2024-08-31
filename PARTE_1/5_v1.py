def latas_restantes(m, j):
    total_latas = m * (m + 1) // 2
    caidas = (m - j) * (m - j + 1) // 2
    latas_pie = total_latas - caidas
    return latas_pie
m, j = map(int, input().split())
print(latas_restantes(m, j))
