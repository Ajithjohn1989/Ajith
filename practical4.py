rows=int(input("enter the number of rows: "))
for r in range(1,rows+1):
   num=r
   d = rows - 1
   for c in range(r):
        print(num,end=" ")
        num+=d
        d-=1
   print("")


