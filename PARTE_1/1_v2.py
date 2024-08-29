print("test")
print("test")
print("test")
print("test")
print("test")
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
        
        bits_to_remove = bin(r - common_bits).count('1')
        results.append(bits_to_remove)
    
    return results

# Casos de prueba proporcionados
test_cases = [(1, 2), (2, 8), (4, 5), (1, 5), (100000, 200000)]

# Obtener los resultados
results = min_elements_to_remove(len(test_cases), test_cases)

# Imprimir los resultados
for result in results:
    print(result)