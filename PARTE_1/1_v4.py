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
data = [
    [11, 13, 11, 11],
    [1, 4, 4, 4, 4],
    [3, 3, 3, 3, 10, 3, 3, 3, 3, 3],
    [20, 20, 10]
]

find_unique_indices(data)



