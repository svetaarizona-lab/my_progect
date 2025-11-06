def square(x:int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    value = begin
    for i in range(end):
        yield value
        value = func(value)

from inspect import isgenerator

gen = some_gen(2, 4, square)
print(isgenerator(gen))# == True, 'Test1'
print (list(gen))# == [2, 4, 16, 256], 'Test2'
print('OK')