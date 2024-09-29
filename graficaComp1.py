import numpy as np
import matplotlib.pyplot as plt

# Definir la función O(n log(log(n)))
def complexity(n):
    return n * np.log(np.log(n))

# Crear un rango de valores de n
n_values = np.linspace(2, 10000, 500)  # Valores de n desde 2 hasta 10000
complexity_values = complexity(n_values)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(n_values, complexity_values, label=r'$O(n \log(\log(n)))$', color='b')
plt.title('Gráfico de O(n log(log(n)))')
plt.xlabel('n')
plt.ylabel('Complejidad')
plt.grid(True)
plt.legend()
plt.show()
