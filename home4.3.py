#Створіть список випадкових чисел від 0 до
# 100 із випадковою кількістю елементів від 3 до 10 (для цього використовуйте бібліотеку random)
import random
n = random.randint(3, 10)
numbers = [random.randint(0, 100) for _ in range(n)]
print("Numbers of elements", n)
print("List", numbers)