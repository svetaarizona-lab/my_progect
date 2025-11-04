# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
#кома, крапка,
def first_word(text: str)-> str:
    """ Пошук першого слова """
    for znak in [",", "."]:
        text = text.replace(znak, " ")
    words = text.split()
    return words [0] if words else ''

print (first_word("Hello world"))# == "Hello", 'Test1'
print (first_word("greetings, friends"))# == "greetings", 'Test2'
print (first_word("don't touch it"))# == "don't", 'Test3'
print (first_word(".., and so on ..."))# == "and", 'Test4'
print (first_word("hi"))# == "hi", 'Test5'
print(first_word("Hello.World"))# == "Hello", 'Test6'
print('OK')