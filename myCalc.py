import math

from Tools.demo.beer import n


def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x/y
def expo(x,y):
    return x**y
def modulo(x,y):
    return x%y
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def sqt(x):
    if x < 0:
        return "Error! Square root of a negative number is not defined."
    else:
        return math.sqrt(x)

def sine(n):
    return math.sin(n)

def log(arg, base):
    return math.log(arg, base)

def is_palindrome(x):
    if x == x[::-1]:
        return "It's a Palindrome."
    else:
        "It's not a Palindrome."

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Comparison")
print("6. Exponential")
print("7. Modulus")
print("8. Factorial")
print("9. Square Root")
print("10. Sine")
print("11. Logarithm")
print("12. Check Palindrome")


while True:
    #Taking input from user
    choice = input("Enter Choice(1/2/3/4/5/6/7/8/9/10/11/12):")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            if num1 > num2:
                print(f"{num1} is greater than {num2}.")
            elif num1 < num2:
                print(f"{num1} is less than {num2}.")
            else:
                print(f"{num1} is equal to {num2}.")

        elif choice == '6':
            print(num1, "Raised to the Power", num2, "=", expo(num1, num2))

        elif choice == '7':
            print("The Modulus of", num1, "with",  num2, "is =", modulo(num1, num2))
    elif choice == '8':
        num = int(input("Enter a number to find its factorial: "))
        print("Result:", factorial(num))

    elif choice == '9':
        num = int(input("Enter a number to find its Square Root: "))
        print("Square Root of the", num, "is:", sqt(num))

    elif choice == '10':
        angle = float(input("Enter Angle:"))
        print("Sin of the Angle", angle, "is:", sine(angle))

    elif choice == '11':
        arg = float(input("Enter Argument:"))
        base = int(input("Enter Base:"))
        print("Log of", arg, "to the Base:", base, "is:", log(arg, base))

    elif choice == '12':
        x = input("Enter Any Number or Word:")
        print(is_palindrome(x))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (Y/N):")
        if next_calculation == "N":
            break

    else:
        print("Invalid Input")


        #creating a armstrong number program in python
        print("Generating:");
        for i in range(1,1000):
            sum = 0
            temp = i
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if i == sum:
                print(i)


