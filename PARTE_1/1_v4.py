def find_unique_indices(data):
    for numbers in data:
        count = {}
        # Contar las ocurrencias de cada número
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        
        # Encontrar el número único
        unique_number = None
        for number in count:
            if count[number] == 1:
                unique_number = number
                break
        
        # Encontrar el índice del número único
        index = numbers.index(unique_number)
        print(index)

# Entrada
t = int(input())
vector=[]
for _ in range(t):
    n = int(input())
    for _ in range (n):
        notas = list(map(int, input().split()))
        vector.append(notas)
    find_unique_indices(vector)
    vector.clear()

    
find_unique_indices(data)



