def prime_generator(end:int ):
    """Генератор простих чисел
    """
    for i in range(2,end+1):
        number = True
        for div  in range(2,int(i**0.5)+1):
            if i % div == 0:
                number = False
                break
        if number:
            yield i

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen))# == True, 'Test0'
print(list(prime_generator(10)))#== [2, 3, 5, 7], 'Test1'
print(list(prime_generator(15)))# == [2, 3, 5, 7, 11, 13], 'Test2'
print(list(prime_generator(29)))# == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')