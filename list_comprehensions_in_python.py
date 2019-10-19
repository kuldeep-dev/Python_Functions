# comprehension in python

# ls = []
# for i in range(100):
#         if i%3==0:
#                 ls.append(i)

# List comprehension 
print("List comprehension")
ls = [i for i in range(100) if i%3==0]  # list comprehensions
print(ls)


# Dictionary comprehension
print("Dictionary comprehension")

mydict = { i:f"item{i}" for i in range(1,5) }
print(mydict)


mydict1 = { i:f"item{i}" for i in range(1,5) }
mydict1 = {value:key for key,value in mydict1.items()}
print(mydict1)



# Set comprehension  # set comprehension duplicate value nhi leta
print("Set comprehension")

dresses = { dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}

print(dresses)
print(type(dresses))


# Generator comprehension
print("Generator comprehension")

evens = (i for i in range(100) if i%2 == 0)
print(type(evens.__next__()))

for items in evens:
        print(items)
