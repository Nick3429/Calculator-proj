# Basic Calculator 
print("Choose Operation")
# addition
def add(a,b):
    return a + b
# subtraction 
def subtract(a,b):
    return a - b
# multiplication
def multiply(a,b):
    return a * b
# division
def divide(a,b):
    return a / b
# Exponent
def exponent(a,b):
    return a**b

choice = ""
while choice!="6":
    print("----------")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponent")
    print("6.End")
    print("----------")

    choice = input("Enter choice ")
    if choice == ("1"):
        num1 = (int(input("Choose your first number ")))
        num2 = (int(input("Choose your second number ")))
        print(add(num1, num2))
    if choice ==("2"):
        num1 = (int(input("Choose your first number ")))
        num2 = (int(input("Choose your second number ")))
        print(subtract(num1, num2))
    if choice == ("3"):
        num1 = (int(input("Choose your first number ")))
        num2 = (int(input("Choose your second number ")))
        print(multiply(num1, num2))
    if choice == ("4"):
        num1 = (int(input("Choose your first number ")))
        num2 = (int(input("Choose your second number ")))
        print(divide(num1, num2))
    if choice == ("5"):
        num1 = (int(input("Choose your first number ")))
        num2 = (int(input("Choose your second number ")))
        print(exponent(num1, num2))









