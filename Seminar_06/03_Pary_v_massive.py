# Задача №43. 
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

from random import randint
n = int(input("Введите размер массива: "))
A = []
for i in range (n):
    A.append(randint(0, 10))
print(A)
s = 0
# №1
# for i in range (n):
#     for j in range (1, n):
#         if i != j and A[i] == A[j]:
#             s += 1
#             print(i, j)
# print(int(s/2))

# №2
for i in range (n):
    for j in range (i+1, n):
        if i != j and A[i] == A[j]:
            s += 1
            # print(i, j)
print(int(s))