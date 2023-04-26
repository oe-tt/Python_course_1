# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# 1

# A = []
# i = 0
# A.append(int(input("Введите число: ")))
# while A[i] != 0:
#     A.append(int(input("Введите число: ")))
#     i += 1
# print(max(A))


# 2

a = int(input("Введите число: "))
max = a
while a != 0:
    a = int(input("Введите число: "))
    if a > max:
        max = a
print(max)


# Ваня:

# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)


# Петя:

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

# У Вани ошибок меньше: только в строке 2 (ограничение максимального элемента) и в строке 5 (неверное условие)
# У Пети ошибки в строке 3 (неверное условие), в строке 6 (неверное присвоение), в строке 7 (неверный вывод)