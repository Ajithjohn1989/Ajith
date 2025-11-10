a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
try:
    c=a/b
    print(c)
except TypeError:
    print("please provide an integer value")
except ZeroDivisionError:
    print("Cannot divide by Zero")