'''
rows = 5
a = 65

for i in range(rows):
    for j in range(i + 1):
        print(chr(a), end=" ")
        a += 1
    print()
'''
'''
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
'''
for num in range (5,0,-1):

   print("* "*num)
