# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите размер массива: "))
A = []
for i in range (N):
    A.append (int(input("Введите число: ")))
print(A)
num = int(input("Введите искомое число: "))
min_razn = abs(max(A) - num)
if num <= min(A):
    bliz = min(A)
    i_bliz = A.index(min(A))
elif num >= max(A):
    bliz = max(A)
    i_bliz = A.index(max(A))
else:
    for i in range(N):
        razn = abs(A[i] - num)
        if razn < min_razn:
            min_razn = razn
            bliz = A[i]
            i_bliz = i

# for i in range(N):
#     razn = abs(A[i] - num)
#     if razn < min_razn:
#         min_razn = razn
#         bliz = A[i]
#         i_bliz = i
        
print(f"Ближайший к числу {num} элемент массива с индексом {i_bliz} равен {bliz}")