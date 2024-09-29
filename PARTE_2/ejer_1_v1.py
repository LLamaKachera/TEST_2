def fibonacci(n):
    fib_sequence = [0, 1]  # Los primeros dos números de Fibonacci
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Ejemplo de uso
n = 10  # Cantidad de términos que deseas generar
resultado = fibonacci(n)
print(resultado)
