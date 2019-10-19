# Super and Overriding in class using python

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        self.classvar1 = "Instance var in Class A"
        self.special = "special"


class B(A):
    calssvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "i am inside class B's constructor"
        self.classvar1 = "Instance var in Class B"
        super().__init__() # supper keyword use for class A


a = A()
b = B()

print(b.special, b.var1 ,b.classvar1)




