#Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
example = [0, 1, 7, 2, 4, 8]
if len (example) ==0:
    result=0
else:
    i = 0
    even_sum = 0
    while i < len(example):
        if i % 2 == 0:
            even_sum += example[i]
        i += 1
        result = even_sum*example[-1]
print("Result:", result)