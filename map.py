#sample program
"""
def multiply(num):
    return num*2
numbers=[34,2,9,1]
for k in numbers:
    print(multiply(k))
"""
#program using map
"""
def multiply(num):
    return num*2
numbers=[34,2,9,1]
print(list(map(multiply,numbers)))
"""
# program using lambda and map
numbers=[34,2,9,1]
print(list(map(lambda num:num*2,numbers)))