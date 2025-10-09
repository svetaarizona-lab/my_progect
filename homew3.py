user = input("Please:  enter the operator (+, -, *, /): ")
num1 = float (input("Please:  enter the first number: "))
num2 = float (input("Please:  enter the second number: "))

if user =="+":
    result = num1 + num2
    print(result)
elif user == "-":
    result = num1 - num2
    print(result)
elif user =="*":
    result= num1 * num2
    print(result)
elif user == "/":
    if num2 == 0:
        print("Error")
    else:
        result = num1 / num2
        print(result)
else:
    print("please enter a valid operator")




