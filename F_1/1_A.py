#funciones donde se encuentra el número único, y devuelve el indice del mismo
def find_unique_indices(data):
    for numbers in data:
        count = {}
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        
        unique_number = None
        for number in count:
            if count[number] == 1:
                unique_number = number
                break
        
        index = numbers.index(unique_number)
        print(index)
        
#entrada de datos con el formato de testeo
t = int(input())
for _ in range(t):
    n = int(input())
    notas = list(map(int, input().split()))
    find_unique_indices([notas])


t = int(input())
a=140
print(a)