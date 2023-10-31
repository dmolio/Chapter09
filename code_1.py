# define a function for addition
def add(num1, num2):
    return num1 + num2

# define a function for subtraction
def subtract(num1, num2):
    return num1 - num2

# define a function for multiplication
def multiply(num1, num2):
    return num1 * num2

# define a function for division
def divide(num1, num2):
    return num1 / num2

# get user input for operation choice and numbers
operation = input("Choose an operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform the chosen operation and print the result
if operation == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("non valid operation")

