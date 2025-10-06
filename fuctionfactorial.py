def fact(num):
    fact=1
    for k in range(1,num+1):
        fact=fact*1
    return fact
num=int(input("enter the number: "))
v=fact(num)
print(f"factorial of {num} is {v}")