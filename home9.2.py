#Є набір чисел (float або int). Вам потрібно знайти різницю
# між найбільшим (максимум) і найменшим (мінімум) елементом.
# Ваша функція difference має вміти працювати з невизначеною кількістю
# аргументів. Якщо аргументів немає, то функція повертає 0 (нуль).
def difference (*args: float):
    if not args: return 0
    result = max(args) - min(args)
    return round(result,2)

print (difference(1, 2, 3)) #== 2, 'Test1'
print (difference(5, -5)) #== 10, 'Test2'
print (difference (10.2, -2.2, 0, 1.1, 0.5)) #== 12.4, 'Test3'
print(difference()) #== 0, 'Test4'

print('OK')