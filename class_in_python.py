#  Classes in python

class Students:
    pass

kuldeep = Students()
sandeep = Students()

kuldeep.name = "Kuldeep"
kuldeep.std = 12
kuldeep.section = "a"
kuldeep.subjects = ["hindi","math","computer"]
print(kuldeep.subjects)


# Instance and class in python


class Employee:
    no_of_leaves = 8
    pass

kuldeep = Employee()
sandeep = Employee()

kuldeep.name = "Kuldeep"
kuldeep.salary = 455
kuldeep.role = "teacher"


sandeep.name = "Sandeep"
sandeep.salary = 855
sandeep.role = "student"

print(kuldeep.name)
print(kuldeep.no_of_leaves)
print(kuldeep.__dict__)
kuldeep.no_of_leaves = 9
print(kuldeep.no_of_leaves)
print(kuldeep.__dict__)
print(Employee.__dict__)
