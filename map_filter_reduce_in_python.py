# Map , Filter and Reduce in python

# Map function
print("Map function")
numbers = ["1","2","3","4","5","6"]

# Normal for loop
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


numbers[2] = numbers[2]+1

print(numbers[2])


# map function using
numbers1 = ["1","2","3","4","5","6"]
numbers = list(map(int,numbers1))
numbers[2] = numbers[2]+1
print(numbers[2])

def sq(a):
    return a*a

num = [2,3,4,5,6,56,67,4,3]
square = list(map(sq,num))
print(square)


# using lambda

num1 = [2,3,4,5,6,56,67,4,3]
square1 = list(map(lambda x:x*x,num1))
print(square1)


def square2(a):
    return a*a

def cube(a):
    return a*a*a

func = [square2 , cube]
num2 = [2,3,4,5,6,56,67,4,3]


for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)



# Filter function
print("Filter function")

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5,list_1))
print(gr_than_5)


# Reduce function
print("Reduce function")

from functools import reduce
list_11 = [1,2,3,4]
num11 = 0
for i in list_11:
    num11 = num11+i
print(num11)    


# using by reduc
prod = reduce(lambda x,y:x+y,list_11)
print(prod)