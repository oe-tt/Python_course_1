# Напишите программу, которая находит все символы, встречающиеся в обеих переданных ей строках.

# Входные данные
# На вход программы подаются две символьные строки, каждая строка завершается символом "конец строки".

# Выходные данные
# Программа должна вывести все символы, которые встречаются в обеих строках, в порядке возрастания их ASCII-кодов. Если таких символов нет, нужно вывести слово 'NO'.

# Примеры
# входные данные:     qwerty      asdqwhy
# выходные данные:    qwy

# входные данные:     qwerty      12345
# выходные данные:    NO

# str_1 = input("Введите строку: ")
# str_2 = input("Введите строку: ")
str_1 = "qwerty"
str_2 = "asdqwhy"
# str_2 = "123456"
set_1, set_2 = set(str_1), set(str_2)
rez = sorted(set_1.intersection(set_2))
if len(rez) > 0:
    print(*rez, end = "")
else:
    print("NO")