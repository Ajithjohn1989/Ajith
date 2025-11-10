#3 methods

#first method
"""
from modulesexamples import add,mul
from moduleseg2 import sub,div
x,y=map(int,input("Enter two numbers: ").split())
print(add(x,y))
print(mul(x,y))
print(sub(x,y))
print(div(x,y))
"""

#second method
# * used to call everything in function
"""
from modulesexamples import *
from moduleseg2 import *
#x,y=map(int,input("Enter two numbers: ").split())
# above syntax can be split for two numbers
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print(add(x,y))
print(mul(x,y))
print(sub(x,y))
print(div(x,y))
"""

#third method
# As a whole module
#but need to call by program name for each function
from package1 import modulesexamples, moduleseg2

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
#or
#x,y=map(int,input("Enter two numbers: ").split())
print(modulesexamples.add(x, y))
print(modulesexamples.mul(x, y))
print(moduleseg2.sub(x, y))
print(moduleseg2.div(x, y))

