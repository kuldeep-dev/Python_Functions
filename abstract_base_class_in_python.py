#  Abstract base class in python

# from abc import ABCMeta,abstractmethod      # abstractmethod is a decorator
# Abstract base class ki obejct nhi bna skte

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()    
print(rect1.printarea())