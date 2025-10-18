#Ваше завдання — написати програму, яка перемножує всі цифри, введені
# користувачем цілого числа, поки воно не стане менше або дорівнювати 9. Введення користувачем

number = int(input("Please:  enter the number:  "))

while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product

print(f"Result: {number} ")