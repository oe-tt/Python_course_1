# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("S: "))
while S < 1 or S > 1000:
    S = int(input("Введите натуральное число S: "))
P = int(input("P: "))
while P < 1 or P > 1000:
    P = int(input("Введите натуральное число P: "))

#1
# i = 1
# for i in range (S):
#     for j in range (S):
#         if (i + j == S) and (i * j == P):
#             print(i, "+", j, "=", S)
#             print(i, "*", j, "=", P)
#             break
#     if (i + j == S) and (i * j == P):
#         break

#2
import math
x = int((S - math.sqrt(S**2-4*P))/2)
y = int((S + math.sqrt(S**2-4*P))/2)
if (x + y == S) and (x * y == P):
    print(x, "+", y, "=", S)
    print(x, "*", y, "=", P)
else:
    print("Введенные числа не корректны")  