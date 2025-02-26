def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

from art import logo as logo

print(logo)

def continue_calculating(number1):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    for operation in operations:
        print(operation)
    user_operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    result = operations[user_operation](number1,number2)
    print(f"{number1}{user_operation}{number2}={result}")
    user_choice = input(f"Type 'y' ro continue with {result} or type 'n' to start a new calculation: ")
    if user_choice == 'y':
        continue_calculating(result)
    elif user_choice == 'n':
        print(10*"\n")
        calculator()

def calculator():
    number1 = float(input("What's the first number?: "))
    continue_calculating(number1)

calculator()
