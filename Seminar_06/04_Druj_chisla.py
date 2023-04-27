# Задача №45. 
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# k = int(input("Введите число <= 105: "))
# while k > 105:
#     k = int(input("Введите число <= 105: "))
# A=[]
# for i in range(2, k):
#     for j in range(i+1, k):
#         summa = 0
#         for z in range(1, j):
#             if j % z == 0:
#                 summa += z
#         if summa == i:
#             A.append([j, i])
# print(A)


# Решение из группы:

# k = int(input('Введите натуральное число: '))
# a = []
# for i in range(3, k + 1):
#     sum = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             sum += j
#     a.append([sum, i])
# print(a)
# c = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i][0] == a[j][1] and a[i][1] == a[j][0] and i !=j and a[i] not in c and a[j] not in c:
#             c.append(a[i])
# print(c)


# k = int(input("Введите число <= 10^5: "))
# while k > 100000:
#     k = int(input("Введите число <= 10^5: "))
# A=[]
# for i in range(2, k):
#     for j in range(i+1, k):
#         summa = 0
#         for z in range(1, j):
#             if j % z == 0:
#                 summa += z
#         rez1 = summa
#         summa = 0
#         for z in range(1, i):
#             if i % z == 0:
#                 summa += z
#         rez2 = summa
#         if rez1 == i and rez2 == j:
#             A.append([i, j])
# print(A)


k = int(input("Введите число <= 10^5: "))
while k > 100000:
    k = int(input("Введите число <= 10^5: "))
A=[]
for i in range(2, k):
    for j in range(i+1, k//2+1):
        summa = 0
        for z in range(1, j):
            if j % z == 0:
                summa += z
        rez1 = summa
        summa = 0
        for z in range(1, i):
            if i % z == 0:
                summa += z
        rez2 = summa
        if rez1 == i and rez2 == j:
            A.append([i, j])
print(A)