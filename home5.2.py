#Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
# - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
while True:
    num1 = float(input("Please:  enter the first number: "))
    num2 = float(input("Please:  enter the second number: "))
    user = input("Please:  enter the user (+, -, *, /): ")

    if user == '+':
        result = num1 + num2
    elif user == '-':
        result = num1 - num2
    elif user == '*':
        result = num1 * num2
    elif user == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Diide by zero cannot !")
            continue
    else:
        print("Unknown!")
        continue

    print("Result :", result)

    again = input("Continue? (y/yes ): ").lower()
    if again not in ("y", "yes"):
        print("THE END ")
        break