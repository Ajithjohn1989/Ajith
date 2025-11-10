from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
         pass
    def orgin(self):
        pass
class B(A):
    def display(self):
        print("Hi")
class C(A):
    def display(self):
        print("Kiwi")
    def orgin(self):
        print("Indian")

ob=B()
ob.display()
obj=C()
obj.orgin()
obj.display()
