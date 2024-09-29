# Función para generar los números de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generamos la secuencia de Fibonacci hasta el número 50
fib_sequence = fibonacci(50)

# Procesar múltiples entradas de prueba
while True:
    try:
        entrada = input()
        if entrada.strip() == "":
            break
        n = int(entrada)
        
        # Verificamos el número en la posición n de Fibonacci
        if n <= 50:
            fib_num = fib_sequence[n]
            if es_primo(fib_num):
                print("Es primo")
            else:
                print("No es primo")
        else:
            print("Probablemente sea primo")
    except EOFError:
        break
