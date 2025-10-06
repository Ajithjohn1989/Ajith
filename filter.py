'''
def even(num):
    if num%2==0:
        return True
    else:
        return False
numbers=[34,2,9,1]
print(list(filter(even,numbers)))
'''
#program with filter and lambda
'''
numbers=[34,2,9,1]
print(list(filter(lambda num:True if num%2==0 else False,numbers)))
'''