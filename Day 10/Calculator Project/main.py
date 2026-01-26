from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

a = int(input("Enter first number: \n"))
operation = input("Enter operation: (+, -, *, /) \n")
if operation not in operations:
    print("Invalid operation. Please try again.")
    quit()
b = int(input("Enter second number: \n"))

print(f"Result is {operations[operation](a, b)}")