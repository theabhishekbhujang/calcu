def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print()

while(True):
    print("Calculator ")
    print()
    print("a. Addition ")
    print("b. Subtraction ")
    print()
    choice = input("Enter your choice: ")
    print()

    match choice:
            
        case 'a':
            print(num1, "+", num2, "=", add(num1, num2))
            print()
        case 'b':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print()
        case 'c':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print()
        case 'd':
            print(num1, "/", num2, "=", divide(num1, num2))
            print()
        case _:
            print("Invalid Input")
            break
