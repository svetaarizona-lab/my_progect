#Клас «Правильний дріб»
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        zmina_a = self.a * other.b + other.a * self.b
        zmina_b = self.b * other.b
        return Fraction(zmina_a, zmina_b)

    def __sub__(self, other):
        zmina_a = self.a * other.b - other.a * self.b
        zmina_b = self.b * other.b
        return Fraction(abs(zmina_a) , zmina_b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(str(f_c))#== 'Fraction: 21, 18'
f_d = f_b * f_a
print(str(f_d)) #== 'Fraction: 6, 18'
f_e = f_b - f_a
print(str(f_e))#== 'Fraction: 3, 18'

print(f_d < f_c)  # True
print(f_d > f_e)  # True
print(f_a != f_b)  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
print(f_1 == f_2)  # True
print('OK')