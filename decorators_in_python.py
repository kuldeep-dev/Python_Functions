# Decorators in python

def function1():
    print("test data")


func2 = function1
del function1
func2()


def functret(num):
    if num == 0:
        return print
    if num == 1:
        return sum

a = functret(1)
print(a)


def executor(func):
    func("this")

executor(print)    


# Decorators
print("Decorators")


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("executed")
    return nowexec

@dec1   # this decorator same as kuldeep = dec1(kuldeep)
def kuldeep():
    print("kuldeep data")

# kuldeep = dec1(kuldeep)
kuldeep()    

