num=int(input("Enter a number: "))
a=int(input("enter a starting number: "))
b=int(input("enter the last number: "))
i=a
print("multi table of {num} from {a} and {b}: ")
while i<=b:
    print(f"{num} x {i} = {num*i}")
    i+=1

