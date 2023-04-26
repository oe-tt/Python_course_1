# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes

def simple(n):
    if n < 4:
        return "yes"
    # for i in range (2, int(pow(n, 0.5))):    # от 2 до квадратного корня из n
    for i in range (2, n):    # от 2 до квадратного корня из n

        if n % i == 0:
            return "no"
    return "yes"

def simple_2(n, i = 2):
    if i > int(pow(n, 0.5)):
        return "yes"
    if n % i == 0:
        return "no"
    return simple_2(n, i+1)

n = int(input("Введите число: "))
print(simple(n))
print(simple_2(n))
# print(int(pow(n, 0.5)))
# print(n**0.5)
# int(pow(n, 0.5)) = n**0.5 = квадратный корень из n