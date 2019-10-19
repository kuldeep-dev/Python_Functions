# Public , Private and Protected class 

class Employee:
    no_of_leaves = 9
    _protect = 9 #  _ single under score means protected variable
    __privat = 98  #  __ double under score means protected variable
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


emp = Employee("Kuldeep", 4565 , "programmer")
print(emp._protect)
# __private is private variable access as _Employee___privat
print(emp._Employee__privat) #name mangling