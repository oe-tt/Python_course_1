class Dragon():
    def __init__(self, height, fire, color):
        self.height = height
        self.fire = fire
        self.color = color
    
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.fire} and color {self.color}."

    def __repr__(self):
        return f"Dragon ({self.height}, {self.fire}, {self.color})"
    
    def change_color(self, new_color):  # замена цвета
        self.color = new_color
        return self.color

    def __add__(self, other):       # суммирование объектов
        other.height = (self.height + other.height) //2
        other.fire = max(self.fire, other.fire)
        other.color = min(self.color, other.color)
        return other

    def __sub__(self, other):      # вычитание
        self.height = self.height // other
        self.fire = self.fire % other
        return self

    def arg_str(self, stroka):  # вызов с аргументом-строкой
        res = ""
        for i in range (self.fire):
            res += stroka
        return res

    def __eq__(self, other):    # сравнение объектов на равенство
        print("Обращение к __eq__!")
        return self.height == other.height and self.fire == other.fire and self.color == other.color
    
    def __le__(self, other):    # сравнение объектов: меньше или равно
        if self.height != other.height:
            return self.height < other.height
        elif self.height == other.height and self.fire != other.fire:
            return self.fire < other.fire
        elif self.height == other.height and self.fire == other.fire and self.color != other.color:
            return self.color < other.color
        else:
            return self.color < other.color
        
    def __gt__(self, other):    # сравнение объектов: больше
        if self.height != other.height:
            return self.height > other.height
        elif self.height == other.height and self.fire != other.fire:
            return self.fire > other.fire
        elif self.height == other.height and self.fire == other.fire and self.color != other.color:
            return self.color > other.color
        else:
            return self.color > other.color
        
dr_1 = Dragon(69, 5, "brown")
dr_2 = Dragon(69, 6, "gray")
dr_3 = Dragon(71, 11, "yellow")
dr_4 = Dragon(50, 10, "wite")
dr_5 = Dragon(70, 4, "black")
dr_6 = Dragon(75, 11, "red")
dr_7 = Dragon(69, 5, "brown")

print()
dr_8 = dr_6 + dr_5
print("dr_6 + dr_5 =", dr_8)
dr_9 = dr_1 + dr_3
print("dr_1 + dr_3 =", dr_9)
dr_10 = dr_1 + dr_4
print("dr_1 + dr_4 =", dr_10)
dr_11= dr_1 + dr_6
print("dr_1 + dr_6 =", dr_11)
dr_12= dr_2 + dr_4
print("dr_2 + dr_4 =", dr_12)
dr_13= dr_2 + dr_6
print("dr_2 + dr_6 =", dr_13)
dr_14= dr_3 + dr_6
print("dr_3 + dr_6 =", dr_14)
dr_15= dr_4 + dr_5
print("dr_4 + dr_5 =", dr_15)

print()
print("dr 1 и 2")
print(dr_1 == dr_2, dr_1 > dr_2, dr_1 < dr_2)
print("dr 1 и 3")
print(dr_1 == dr_3, dr_1 > dr_3, dr_1 < dr_3)
print("dr 1 и 4")
print(dr_1 == dr_4, dr_1 > dr_4, dr_1 < dr_4)
print("dr 1 и 5")
print(dr_1 == dr_5, dr_1 > dr_5, dr_1 < dr_5)
print("dr 1 и 6")
print(dr_1 == dr_6, dr_1 > dr_6, dr_1 < dr_6)
print("dr 1 и 7")
print(dr_1 == dr_7, dr_1 > dr_7, dr_1 < dr_7)

print()
print(dr_1, dr_2, dr_3, sep="\n")
print()
print(" dr_1 =", repr(dr_1), "\n", "dr_2 =", repr(dr_2), "\n", "dr_3 =", repr(dr_3), "\n")

dr_5.change_color("blue")
print(dr_5)
print()
print(dr_7.arg_str("Hello! "))
print(dr_4.arg_str("Hi :) "))

print()
print(dr_3 - 20)
print(dr_5 - 10)