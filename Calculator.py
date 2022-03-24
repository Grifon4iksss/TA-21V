operation = input("Please write +, /, *, **, //, % or - to pick calculator: ")

if operation == "+":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 + num2)

if operation == "-":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 - num2)

if operation == "/":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 / num2)

if operation == "*":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 * num2)

if operation == "**":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 ** num2)

if operation == "//":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 // num2)

if operation == "%":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 % num2)