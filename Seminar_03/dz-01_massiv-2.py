# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 1 
N = int(input("Введите размер массива: "))
A = []
for i in range (N):
    A.append (int(input("Введите число: ")))
print(A)
num = int(input("Введите искомое число: "))
count = 0
for i in range(N):
    if A[i] == num:
        count += 1
print(f"Число {num} встретилось в массиве {count} раз")


# 2
# N = int(input("Введите размер массива: "))
# A = []
# for i in range (N):
#     A.append (int(input("Введите число: ")))
# print(A)
# num = int(input("Введите искомое число: "))
# count = A.count(num)
# print(f"Число {num} встретилось в массиве {count} раз")