# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

N = int(input("Введите число: "))
while N <= 0:
    N = int(input("Введите положительное число: "))
i = 1
F = 1
while i <= N:
    F *= i
    i += 1
print ("факториал числа ", N, "=", F)