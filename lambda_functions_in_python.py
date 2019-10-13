# lambda functions or anonymous functions  in python 

def add(a,b):
    return a+b


minus = lambda x,y:x-y 

# same as

def minus1(a,b):
    return a-b


print(minus(8,4))    

# Normal function
def a_first(a):
    return a[1]

# list
a = [[1,14],[5,6],[8,23]]
a.sort(key = a_first)
print(a)



# using lambda
a = [[1,14],[5,6],[8,23]]
a.sort(key = lambda x:x[1])
print(a)



