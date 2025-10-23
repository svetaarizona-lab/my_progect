#Написати функцію say_hi, яка представить людину за переданими параметрами.
#Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
#Функція має повернути рядок.
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print("OK")