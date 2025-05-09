def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b  # ZeroDivisionError 가능성 있음

def multiply(a, b):
    return a * b

def main():
    print("Welcome to the calculator!")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    
    print("Choose operation: 1) Add  2) Subtract  3) Multiply  4) Divide")
    choice = input("Your choice: ")

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice.")

main()
