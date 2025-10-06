"""num=int(input("Enter the number: "))
fact=1
for k in range(1,num+1):
    fact=fact*k
print(f"Factorial of {num} is {fact}")
"""
num=int(input("Enter the number: "))
fact=1
counter=0
while True:
    fact=fact*num
    fact+=1
    print(fact)
