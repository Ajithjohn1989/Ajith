'''

x = "awesome"

def myfunc():
   x = "fantastic"
   print("Python is " + x)

myfunc()
print("Python is " + x)
'''
'''
def greeting(first, last):

  def getFullName():
   return first + " " + last

  print("Hi, " + getFullName() + "!")

greeting('Quincy', 'Larson')
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Now you have to call the function
#you can choose any value of n, let say 5
fact = factorial(5)
print(fact)