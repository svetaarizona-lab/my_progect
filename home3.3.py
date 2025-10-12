example = [1] , [], [[1, 2, 3], [4, 5, 6]] # можна змінювати для перевірки

if not example:
    pr = [[], []]
    print("empty list", pr)
else:
    middle = len(example) // 2 #middle of the list
    if len(example) % 2 == 0: #even numbers
        first = example[:middle]
        second = example[middle:]
        pr = [first, second]
        print("even numbers", pr)
    else: #odd numbers
        first = example[:middle]
        second = example[middle:]
        pr = [first, second]
        print("odd numbers", pr)