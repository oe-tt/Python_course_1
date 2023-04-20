# Напишите программу, которая вычисляет двойной факториал натурального числа N ( 1 ≤ N ≤ 10000 ), сохранив все значащие цифры. 
# Двойным факториалом N !! называется произведение натуральных чисел через одно от 1 (для нечётного числа) или от 2 (для чётного числа) 
# до N : N !! = 1·3·5... ( N - 2)· N , если N – нечётное и N !! = 2·4·6... ( N - 2)· N , если N – чётное.

# Входные данные
# Входная строка содержит натуральное число N ( 1 ≤ N ≤ 10000 ).

# Выходные данные
# Программа должна вывести двойной факториал числа N .

# Примеры
# входные данные
# 7
# выходные данные
# 105
# входные данные
# 8
# выходные данные
# 384

a = int(input("Введите число: "))
if a % 2 != 0:
    i = 1
else:
    i = 2
F = 1
while i <= a:
    F *= i
    i += 2 
print(F)