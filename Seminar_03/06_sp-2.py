# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# N = 10
# A = []
# from random import randint
# for i in range (N):
#     A.append(randint(0, 10))
# print(A)
# B = set(A)
# print(len(B))

# 2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

N = 10
A = []
from random import randint
for i in range (N):
    A.append(randint(0, 10))
print(A)
A.sort()
print(A)
i = 1
max_count = 0
count = 0
while i < N:
    if A[i] == A[i-1]:
        count += 1
        # if count > max_count:
        #     max_count = count
    i += 1
# print(max_count)
print(count)

# B = set(A)
# print(len(A) - len(B))

