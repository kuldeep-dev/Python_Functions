# Operators overloading and Dunder method in python

# jo __ (under score under score se start hone vale mrthods ko kehte h dunder methods)

class Employee:
    no_of_leaves = 9
    def __init__(self , aname ,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"name is {self.name} , salary is {self.salary} , role is {self.role}"

    @classmethod
    def change_leaves(cls , new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self,other):   #Special add dunder method for help in operator overloading
        return self.salary + other.salary

    # true division operator overloading
    def __truediv__(self,other):
        return self.salary / other.salary

    # repr method
    def __repr__(self):
        return self.printdetails()

    def __str__(self):
        return f"str method name is {self.name} , salary is {self.salary} , role is {self.role}"     

emp1 = Employee("Kuldeep",7585,"teacher")
emp2 = Employee("sachin",785,"student")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)
print(repr(emp1))