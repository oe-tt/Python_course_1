from random import randint
import statistics

class Human():
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grades

    def __str__(self):
        return f"Имя: {self.name} {self.surname}, возраст: {self.age} лет"
    
    def greet(self):
        return f"Привет! Меня зовут {self.surname} {self.name}, мне {self.age} лет"
    
    def __repr__(self):
        return self.name
    
    def avg_score(self):
        return statistics.mean(self.grades)
    

ivan = Human("Ivan", "Petrov", 15, [])
petr = Human("Petr", "Ivanov", 16, [])
vasya = Human("Vasiliy", "Zaharov", 17, [])
dima = Human("Dmitriy", "Fedorov", 18, [])
fedya = Human("Fedor", "Vasiliev", 19, [])
stas = Human("Stas", "Makarov", 20, [])


lst = [ivan, petr, vasya, dima, fedya, stas]
print(*lst)

for i in lst:
    i.grades = [randint(1,5) for j in range (10)]

lst.sort(key = lambda y: y.avg_score())
print("\n Отсортированный список: \n")
print(*lst)
print("")
print(petr)
print(petr.greet())
print(petr.grades)
print(petr.avg_score())