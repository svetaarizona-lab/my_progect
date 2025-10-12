example = [1, 2, 3, 4, 5, 6]
if len(example) == 0: #порожній
    result = [[], []]
    print("Порожній:", result)
else:
    middle = len(example) // 2 #середина
    if len(example) % 2 != 0: #непарна
        middle += 1
    first = example[:middle]
    second = example[middle:]
    result = [first, second]
    print("Результат:", result)