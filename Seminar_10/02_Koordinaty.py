class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a_koord(self):
        return [a.x, a.y, b.x, b.y]
    
    def area(self):
        return abs(b.x - a.x) * abs(b.y - a.y)

    def perimetr(self):
        return (abs(b.x - a.x) + abs(b.y-a.y)) * 2
    

    def has_point(self, point):
        if (point.x < max(a.x, b.x) and point.y < max(a.y, b.y) and point.x > min(a.x, b.x) and point.y > min(a.y, b.y)):
            return True
        else:
            return False

    
class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y


a = Point(1, 10)
b  = Point(10, 1)

tochka_1 = Point(5, 5)
tochka_2 = Point(10, 10)
pryamougolnik = Rectangle(a, b)

print(f"Площадь прямоугольника = {pryamougolnik.area()}")
print(f"Периметр прямоугольника = {pryamougolnik.perimetr()}")

print(f"Точка {tochka_1.x}.{tochka_1.y} находится внутри прямоугольника: {pryamougolnik.has_point(tochka_1)}")
print(f"Точка {tochka_2.x}.{tochka_2.y} находится внутри прямоугольника: {pryamougolnik.has_point(tochka_2)}")