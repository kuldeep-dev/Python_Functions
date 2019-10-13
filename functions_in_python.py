# Functions

a = 9
b =8
c = sum((a,b)) # built in function
print(c)


# user defined functions

def funstion1():
    print("You are in function1")

print(funstion1())
funstion1()


def funstion2(a,b):
    print("You are in function2",a+b)


funstion2(4,6)


def function3(a,b):
    """ this is a function return average of two numbers  """
    average = (a+b)/2
    # print(average)
    return average

v = function3(4,6)

print(v)

print(function3.__doc__)


#  Try and Catch 
#  Error Handling

print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()

try:
    print("Sum of these two numbers",int(num1) + int(num2))
except Exception as e:
    print(e)    


    