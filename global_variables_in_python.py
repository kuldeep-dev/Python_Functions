# Global variables in python


l = 10 # Global variable
def function1(n):
    n = 5 # local variable
    global l  # use global keyword for change the number 
    l = l + 4 
    print(l)
    print(n,"Printed")

function1("adfd")
print(l)

#  Nested function

x = 89
def kuldeep():
    x = 20
    def newdata():
        global x
        x = 88
    print("before call newdata",x)
    newdata()
    print("after call newdata",x)

kuldeep()
print(x)
