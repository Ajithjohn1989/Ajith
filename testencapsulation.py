class __Animal:
    def sound(self,name,color):
         self.__name="Tiger"
         self.__color="brown&black"


class Dog(Animal):
    def sound(self):
         return "Bark"
    print("Bark")

class Cat(Animal):
    def sound(self):
         return "Meow"
    print("Meow")
c=Cat()
c.sound()
d=Dog()
d.sound()
ob=Animal()
print(ob._A__sound)