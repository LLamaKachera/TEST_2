def count_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def min_elements_to_remove(t, test_cases):
    results = []
    
    for _ in range(t):
        l, r = test_cases[_]
        common_bits = 0
        
        for i in range(20):  # Considerando enteros de hasta 2*10^5, lo cual requiere alrededor de 20 bits para representar.
            mask = 1 << i
            if l & mask == r & mask:
                common_bits |= (l & mask)
            else:
                break
        
        bits_to_remove = count_bits((r ^ common_bits) + 1) - count_bits(common_bits)
        results.append(bits_to_remove)
    
    return results

# Lectura de la entrada
t = int(input())
test_cases = []
for _ in range(t):
    l, r = map(int, input().split())
    test_cases.append((l, r))

# Obtener los resultados
results = min_elements_to_remove(t, test_cases)

# Imprimir los resultados
for result in results:
    print(result)