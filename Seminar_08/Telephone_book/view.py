# view.py - функции для работы с пользователем (интерфейс)
import database

def user_input():
    # ask = int(input("Выберите пункт меню:\n", "1 - Создать контакт\n", "2 - Добавить данные\n", "3 - Поиск (по имени или телефону)\n", 
    #             "4 - Сортировка (по имени или дате рождения)\n", "5 - Вывод только имен сотрудников\n", "6 - Вывод всей телефонной книги\n"))
    ask = int(input("""\nВыберите пункт меню:\n 1 - Создать контакт\n 2 - Поиск (по имени или телефону)\n 3 - Изменить контакт
 4 - Удалить контакт\n 5 - Сортировка (по имени или дате рождения)
 6 - Вывод только имен сотрудников\n 7 - Вывод всей телефонной книги\n 8 - Выход\n"""))
    return ask

def input_kontact():
    kontakt = list()
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    date = input("Дата рождения: ")
    telephone = input("Телефон: ")
    
    kontakt = surname + " " + name + " " + patronymic + ", d.r.: " + date + ", tel.: " + telephone + "\n"
    return kontakt

def poisk():
    str_poisk = input("Введите данные для поиска: ")
    return str_poisk

def izmen():
    print("Выберите контакт для внесения изменений.")
    search_str = poisk()    # ищем строку (по ее части) для внесения изменений
    search_ok = database.search_kontakt(search_str)     # нашли строку для внесения изменений
    print("Найден контакт:")
    print(search_ok)
    data = list(search_ok.split())      # сформировали список из найденной строки
    # print(search_str)
    print("Выберите, какие данные хотите изменить:")
    izm = int(input(""" 1 - Изменить имя\n 2 - Изменить фамилию\n 3 - Изменить отчество
 4 - Изменить дату рождения\n 5 - Изменить телефон\n"""))
    if izm == 1:
        data[1] = input("Введите имя: ")
    elif izm == 2:
        data[0] = input("Введите фамилию: ")
    elif izm == 3:
        data[2] = input("Введите отчество: ")
    elif izm == 4:
        data[4] = input("Введите дату рождения: ")
    else:
        data[6] = input("Введите телефон: ")
    print("Изменения внесены:")
    # print(data)     
    data_str = " ".join(data)   # сформировали строку с изменениями
    data_str += "\n"
    print(data_str)
    return search_ok, data_str

# ask = user_input()
# ask = user_input()
# kontakt = input_kontact()
# print(kontakt)

def udalenie():
    print("Выберите контакт, который нужно удалить.")
    search_str = poisk()    # ищем строку (по ее части)
    search_ok = database.search_kontakt(search_str)     # нашли строку для удаления
    print("Найден контакт:")
    print(search_ok)
    return search_ok    

def sposob():
    print("Выберите способ сортировки данных:")
    spos = int(input(" 1 - Сортировка по имени\n 2 - Сортировка по фамилии\n 3 - Сортировка по дате рождения\n"))
    return spos