def checker(fun):
    def wrapper(a,b):
        if a>b:
            return fun(a,b)
        else:
            return "a is smaller"
    return wrapper
@checker
def substract(a,b):

    return a-b
print(substract(5,7))
