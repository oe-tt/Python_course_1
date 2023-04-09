# Найдите сумму цифр трехзначного числа.

num = input("Введите трехзначное число >> ")
while int(num) < 100 or int(num) > 999:
    num = input("Ошибка! Введите трехзначное число >> ")
sum_num = int(num[0]) + int(num[1]) + int(num[2])
print(f"Сумма цифр числа {num} = {sum_num}")