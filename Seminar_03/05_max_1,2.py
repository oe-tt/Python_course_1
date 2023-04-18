# 3.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

N = 10
A = []
from random import randint
for i in range (N):
    A.append(randint(0, 10))
print(A)
max_1 = max_2 = 0
for i in range (N):
    if A[i] > max_1:
        max_2 = max_1
        max_1 = A[i]
    elif A[i] > max_2 and A[i] < max_1:
        max_2 = A[i]
print(f"max_1 = {max_1}, max_2 = {max_2}")
