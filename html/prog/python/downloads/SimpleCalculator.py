# Just a Simple Calculator, With Tips and Sales Tax

# Function for Addition
def add(num1, num2):
    return num1 + num2

# Function for Subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for Multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for Division (And not by zero)
def divide(num1, num2):
    return num1 / num2

# The entire programmed is looped so it will continue after you make a calculation
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Sales Tax Cal")
    print("6.Tip cal(15%)")
    print("7.Pi")
    print("8.Exit")
    
# This interprets the input and executes commands based on the input
    choice = input("Enter choice(1/2/3/4/5/6/7/8):")

    if choice == '8':
        print("Ending Program")
        print(" ")
        break
# To end the program you need to break the loop

    if choice == '1':
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print(num1,"+",num2,"=", add(num1,num2))
        print(" ")
        
    elif choice == '2':
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print(num1,"-",num2,"=", subtract(num1,num2))
        print(" ")

    elif choice == '3':
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print(num1,"*",num2,"=", multiply(num1,num2))
        print(" ")
        
    elif choice == '4':
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print(num1,"/",num2,"=", divide(num1,num2))
        print(" ")
        
    if choice == '5':
        num3 = int(input("Enter price: "))
        print(num3,"*",0.06,"=", multiply(num3,0.06))
        print(" ")
        
    if choice == '6':
        num4 = int(input("Enter price: "))
        print(num4,"*",0.15,"=", multiply(num4,0.15))
        print(" ")
        
    if choice == '7':
        print("Unfortunately I couldnt find a Pie.")
        print(" ")
    
