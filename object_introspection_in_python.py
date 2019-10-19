#   Object Introspection in oops using python


class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"  

    @property  #decorator property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("setting now..")
        names = string.split("@")[0]
        fname = names.split(".")[0]
        lname = names.split(".")[1]
        
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

kuldeep = Employee("kuldeep","kumar")
sandeep = Employee("sandeep","kumar")

print(kuldeep.email)
print(dir(kuldeep))
print(type(kuldeep)) # this is object introspection
print(type("this is class"))
print(id("this is class"))

o = "this is a object"
print(dir(o))

print("inspect module")

import inspect

print(inspect.getmembers(kuldeep))