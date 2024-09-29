import time

def criba(n):
    primo = [True] * (n + 2)
    primo[0] = primo[1] = False
    i = 2
    while i * i <= n:
        if primo[i]:
            for j in range(i * i, n + 1, i):
                primo[j] = False
        i += 1
    return primo

def main():
    n = 5000
    primo = [True] * (n + 2)
    
    # Primera llamada a la función Criba
    criba(n)
    
    # Medición de tiempo
    a = time.time_ns()
    criba(n)
    b = time.time_ns()
    
    # Diferencia de tiempo en nanosegundos
    d = b - a
    print(d)

if __name__ == "__main__":
    main()
