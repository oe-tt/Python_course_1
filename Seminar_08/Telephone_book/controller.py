# controller.py - связь функций между собой

import view
import database

def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            new_kontakt = view.input_kontact()
            print(new_kontakt)
            database.add_kontakt(new_kontakt)
        elif ask == 2:
            search = view.poisk()
            print(database.search_kontakt(search))
        elif ask == 3:
            old_str, new_str = view.izmen()
            database.zamena_str(old_str, new_str)
            # print(new_str)
        elif ask == 4:
            delete_str = view.udalenie()
            database.udalen_str(delete_str)
            # print(new_str)        
        elif ask == 5:
            # sposob_sort = view.sposob()
            database.sortirovka(view.sposob())
        elif ask == 6:
            database.print_names()
        elif ask == 7:
            database.all_book()
        elif ask == 8:
            break

main()

