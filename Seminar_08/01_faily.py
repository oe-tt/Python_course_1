with open("file.txt", "w") as file:
    a = ["1\n", "2\n", "3\n"]
    file.writelines(a)

with open("file.txt", "r") as file:
    print(file.read())

# или так:
# но тогда надо использовать метод "strip()", чтобы убрать лишние пустые строки (символы "\n").
with open("file.txt", "r") as file:
    for i in range(3):
        print(file.readline().strip())

# или так:
# но тогда надо пеерместить курсор в начало файла:
    file.seek(0)    # перемещает курсор на указанную позицию
    print(file.read())

# или так:
    file.seek(0)
    print(file.readlines())    # читает все строки файла, и каждую помещает как элемент в список.

    file.seek(0)
    lst = file.readlines()     # список со строками
    print(*lst)