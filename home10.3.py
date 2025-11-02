#Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
#Вхідні дані: Ціле число.
#Вихідні дані: Логічний тип.

def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число
    :digit :ціле число
    :return : True or False """
    return digit % 2 == 0
print(is_even(2)) #== True, 'Test1'
print(is_even(5)) #== False, 'Test2'
print(is_even(0))#== True, 'Test3'
print('OK')