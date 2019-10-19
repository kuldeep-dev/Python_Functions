# Generators in python

"""
Iterable -- __iter__() or __getitem__() method hote h  
Iterator -- __next__() 
Iteration --


string Iterable hota h
integer Iterable nhi hota 

"""

""" 
Generators ek trah k itrable hote h

yield is a generator

"""

for i in range(20):
        print(i)


def gen(n):
        for i in range(n):
                yield i

g = gen(2)
print(g.__next__())
print(g.__next__())                

k = "kuldeep"
for c in k:
        print(c)

ier = iter(k)
print(ier.__next__())        