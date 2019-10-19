# Multiple Inheritance in opps using python

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

class Player:
    var = 9
    no_of_game = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"name is {self.name} , game is {self.game}"    

class CoolProgrammer(Employee,Player):
    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)



print("Multiple Inheritance")

amit = Employee("Amit",4695 , "teacher")
sandeep = Employee("sandeep",9632 , "student")

sachin = Player("sachin",["cricket"])
karan = CoolProgrammer("karan",4569,"coolprogrammer")
# det = karan.printdetails()
# karan.printlanguage()
# print(det)

print(karan)



# Diamond Problem in multiple Inheritence

print("Diamond Problem in multiple Inheritence")

class A:
    def med(self):
        print("This is a method from A")

class B(A):
    def med(self):
        print("This is a method from B")

class C(A):
    def med(self):
        print("This is a method from C")

class D(B,C):
    def med(self):
        print("This is a method from D")


a = A()
b = B()
c = C()
d = D()

d.med()