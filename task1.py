num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

switch = input("Enter the operation (+, -, *, /): ")
if switch == "+":
    result = num1 + num2
    print("Addition:", result)
elif switch == "-":
    result = num1 - num2
    print("Subtraction:", result)
elif switch == "*":
    result = num1 * num2
    print("Multiplication:", result)
elif switch == "/":
    if num2 != 0 :
        result = num1 / num2
        print("Division:", result)
    else:
        print("Error: Division by zero is not allowed.")