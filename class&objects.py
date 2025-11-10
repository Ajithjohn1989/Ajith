'''
class fruit:
    orgin="India"#class variable

    def details(self,a,b):
        self.name=a
        self.state=b
fruit1=fruit()#object creation
fruit2=fruit()#object creation
fruit1.details("apple","Himachal pradesh")#Assing value to objects
fruit2.details("Grapes","Tamil Nadu")
print(fruit.orgin)#Acessing class variable
print(fruit1.state)
print(fruit1.name,fruit1.state)
'''
# USAGE of __init__
#using __init causes automatic call when an object is created in class
class fruit:
    orgin="India"#class variable

    def __init__(self,a,b):
        self.name=a
        self.state=b

