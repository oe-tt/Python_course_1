# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def stepen(a, b):
    s = 1
    if b == 1:
        return a
    return a * stepen(a, b-1)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(stepen(a, b))
