x=int(input("Enter the first divisible: "))
y=int(input("Enter the second divisible: "))
n=int(input("Enter the no:of times: " ))
num=1
counter=0
while True:
 if num%x==0 and num%y==0:
     counter=counter+1
     print(num,end=" ")
     if counter==n:
         break
 num+=1