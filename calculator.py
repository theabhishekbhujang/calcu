def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multi(a, b):
    return a * b
def divi(a, b):
    return a /  b
print()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print()

while(True):
    print("Calculator ")
    print()
    print("a. Addition ")
    print("b. Subtraction ")
    print("c. Multiplication ")
    print("d. Division ")
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
            print(num1, "*", num2, "=", multi(num1, num2))
            print()
        case 'd':
            print(num1, "/", num2, "=", divi(num1, num2))
            print()
        case _:
            print("Invalid Option ")
            break
