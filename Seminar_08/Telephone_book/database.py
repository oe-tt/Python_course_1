# database.py - функции для работы с текстовым файлом

def add_kontakt(new_kontakt):
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "a") as file:
        file.writelines(new_kontakt)
    print("Телефонная книга обновлена.")

def search_kontakt(poisk):
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if poisk in i:
                flag = True
                return i
        if flag == False:
            return "Данные не найдены"

def zamena_str(old, new):
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r+") as file:
        data = file.read()         # считываем данные из файла
        data = data.replace(old, new)   # заменяем строки
        file.seek(0)                    # перемещаем курсор в начало
        file.write(data)
    # print("Телефонная книга обновлена.")

def udalen_str(delete_str):
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r") as file:
        data = file.readlines()
    delete_str = "".join(delete_str)
    print(delete_str)
    i = data.index(delete_str)
    del data[i]
    print(data)
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "w") as file:
        file.writelines(data)
    print("Контакт удален")

# def udalen_str(delete_str):
#     with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r+") as file:
#         data = file.readlines()
#         delete_str = "".join(delete_str)
#         print(delete_str)
#         i = data.index(delete_str)
#         del data[i]
#         print(data)
#         file.seek(0)
#         file.writelines(data)
#     print("Контакт удален")

def sortirovka(sposob):
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r+") as file:
        data = file.readlines()
    if sposob == 2:     # сортировка по фамилии
        # new_data = str(sorted(data))
        with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "w") as file:
            data.sort()
            file.writelines(data)
        print(data)
            # new_data = "\n".join(sorted(data))
            # new_data = new_data.replace("\n\n", "\n")
            # file.writelines(new_data)
            # print(new_data)
    if sposob == 1:     # сортировка по имени
        with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "w") as file:
            for i in range(len(data)):
                data[i] = list(data[i].split())
            data.sort(key = lambda x: x[1])
            for i in range(len(data)):
                data[i] = " ".join(data[i]) + "\n"
            file.writelines(data)
        print(data)
    
    if sposob == 3:     # сортировка по дате рождения
        with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "w") as file:
            for i in range(len(data)):
                data[i] = list(data[i].split())
            data.sort(key = lambda x: x[4])
            for i in range(len(data)):
                data[i] = " ".join(data[i]) + "\n"
            file.writelines(data)
        print(data)

def print_names():
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r") as file:
            data = file.readlines()
            for i in data:
                print(i.split()[1])

def all_book():
    with open("E:/2022/Python/Course_1/Seminar_08/Telephone_book/tel_book.txt", "r+") as file:
        data = file.read()
        print(data)

