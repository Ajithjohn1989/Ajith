class Animal:
    def sound(self):
        return "Some generic sound"

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