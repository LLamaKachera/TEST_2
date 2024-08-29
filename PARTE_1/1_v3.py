def find_unique_index(n, notes):
    # Encontrar el elemento único comparando los primeros 3 elementos
    unique_element = None
    for i in range(2, n):
        if notes[i] != notes[i - 1]:
            if notes[i] == notes[i - 2]:
                unique_element = notes[i - 1]
            else:
                unique_element = notes[i]
            break

    # Encontrar el índice del elemento único
    for i, note in enumerate(notes):
        if note != unique_element:
            return i

# Lectura de la entrada
t = int(input())
for _ in range(t):
    n = int(input())
    notes = list(map(int, input().split()))

    # Encontrar e imprimir el índice del elemento único
    print(find_unique_index(n, notes))