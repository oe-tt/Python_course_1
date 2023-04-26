# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    if b == 0:
        return a
    return summa(a+1, b-1)

a = int(input("a = "))
while a < 0:
    a = int(input("a < 0! a = "))
b = int(input("b = "))
while b < 0:
    b = int(input("b < 0! b = "))
print(summa(a, b))