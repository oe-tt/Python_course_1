# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

A = int(input("Введите натуральное число: "))
while A < 1:
    A = int(input("Введите натуральное число! "))
i = 2
num_pred_pred = 0
num_pred = 1
num = 1
while num < A:
    num = num_pred_pred + num_pred
    num_pred_pred = num_pred
    num_pred = num
    print (num)
    i += 1
if A == num:
    print(f"Число {A} в последовательности Фибоначчи на позиции № {i}")
else:
    print("-1")
