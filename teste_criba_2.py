def Criba(n):                      # Complejidad: O(1)
    primo[0] = primo[1] = False     # O(1)
    i = 2                           # O(1)
    while i * i <= n:               # Este bucle depende de la raíz cuadrada de n, por lo que la complejidad será O(√n)
        if primo[i]:                # O(1)
            for j in range(i * i, n+1, i):  # Este bucle itera sobre los múltiplos de i, lo que tiene una complejidad de O(n/i)
                primo[j] = False    # O(1)
        i = i + 1                   # O(1)

n = 25                              # O(1)
primo = [True] * (n+2)              # Crear una lista con n+2 elementos es O(n)
Criba(n)                            # La función `Criba(n)` tiene una complejidad total de O(n log(log(n)))
for i in range(2, n):               # Este bucle itera desde 2 hasta n, por lo que su complejidad es O(n)
    if primo[i]:                    # O(1)
        print(i)                    # O(1)
