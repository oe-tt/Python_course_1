# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

s_1 = input("Введите текст: ")
s_1 = s_1.lower().split()
s_2 = set(s_1)
# print(s_2)
print(len(s_2))

