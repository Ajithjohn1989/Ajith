"""
rows = 5
a = 65
for i in range(rows):
    for j in range(i + 1):
        print(chr(a), end=" ")
        a += 1
    print()
"""
rows = 5
for r in range(rows):
    num=65
    d=1
    for c in range(r):
        print(chr(num), end=" ")
        num+=d
    print()