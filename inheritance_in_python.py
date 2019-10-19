# Single Inheritance in opps using python

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
        return cls(*string.split("-"))

    @staticmethod    #Static methods oops 
    def printgoods(string):
        print("This is good" + string)
        # return "kuch b"


print("Single Inheritance")
class Programmer(Employee):
    def __init__(self , aname ,asalary,arole , languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"programmer name is {self.name} , salary is {self.salary} , role is {self.role} , languages are {self.languages}"
    

amit = Employee("Amit",4695 , "teacher")
sandeep = Employee("sandeep",9632 , "student")

sachin = Programmer("Sachin", 7896 , "programmer" , ["python","c++","php"])
karan = Programmer("Karan", 8526, "programmer", ["python","c++","php"])


print(karan.printprog())