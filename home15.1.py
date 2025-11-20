#Клас Прямокутник
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        area = self.get_square() + other.get_square()
        return Rectangle(area, 1)

    def __mul__(self, n):
        area = self.get_square() * n
        return Rectangle(area, 1)


    def __str__(self):
        return f"Rectangle({self.width} x {self.height}), area={self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square()) #== 8, 'Test1'
print(r2.get_square())# == 18, 'Test2'

r3 = r1 + r2
print(r3.get_square())# == 26, 'Test3'

r4 = r1 * 4
print(r4.get_square())# == 32, 'Test4'

print( Rectangle(3, 6) == Rectangle(2, 9),)# 'Test5'