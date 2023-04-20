# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: aaabcaadcdd
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# # 1
# print("**********************************")
# s = "aaabcaadcdd"
# # s = input("Введите строку").split()
# for i in range (len(s)):
#     count = 0
#     for j in range(i):
#         if s[j] == s[i]:
#             count += 1
#     if count == 0:
#         print(s[i], end=" ")
#     else:
#         print(f"{s[i]}_{count}", end=" ")

# Решение работает, но высокая сложность: если будет миллион символов то нужно будет миллион в квадрате проходов...


# 2
print("**********************************")
s = "aaabcaadcdd"
# s = input("Введите строку").split()
count = dict()
for i in s:
    if i in count:
        count[i] += 1   # обращаемся к значению словаря по его ключу. Ключ здесь = i
        print(f"{i}_{count[i]}", end = " ") 
    else:
        count[i] = 0
        print(i, end = " ") 

