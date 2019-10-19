# Constructor in python

class Employee:
    no_of_leaves = 9
    def __init__(self , aname ,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"name is {self.name} , salary is {self.salary} , role is {self.role}"

# kuldeep = Employee()
# sandeep = Employee()
amit = Employee("Amit",4695 , "teacher")

# kuldeep.name = "Kuldeep"
# kuldeep.salary = 455
# kuldeep.role = "teacher"


# sandeep.name = "Sandeep"
# sandeep.salary = 855
# sandeep.role = "student"

# print(kuldeep.printdetails())
# print(kuldeep.no_of_leaves)


# using Contructor
print("using Contructor")


print(amit.salary)