# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

def zamena(array):
    J_min = min(array)
    J_max = max(array)
    for i in range(len(array)):
        if array[i] == J_max:
            array[i] = J_min
    return array
            
Jurnal = [1, 3, 3, 2, 3, 4, 4]
print(zamena(Jurnal))
