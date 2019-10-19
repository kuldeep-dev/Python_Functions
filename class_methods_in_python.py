#  Class methods in python


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

    @classmethod
    def from_str(cls , string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])    
        return cls(*string.split("-"))

    @staticmethod    #Static methods oops 
    def printgoods(string):
        print("This is good" + string)
        # return "kuch b"


amit = Employee("Amit",4695 , "teacher")
sandeep = Employee.from_str("sandeep-564-student")

amit.change_leaves(32)


print(amit.no_of_leaves)


# Alternative class methods
print("Alternative class methods")

print(sandeep.salary)


# Static methods oops in python
print("Static methods oops in python")

print(sandeep.printgoods("kuldeep"))


# Abstraction and Encapsulation in python

