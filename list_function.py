#  List datatype

subjects = ["math","hindi","science","economics","computer"]
print(subjects[1]) # access list items

numbers = [2,7,9,11,3]
print(numbers[2])  # access list items

# list methods
print("list methods")
numbers.sort() # sort number in a accending order
print(numbers)

numbers.reverse() # sort number in a decending order
print(numbers)


# Slicing in list
print("Slicing in list")
print(numbers[:5]) # reverse the list

#  slicing always return new list

# extended Slice
print("extended Slice")
print(numbers[::2]) # skip one number between the list

print(max(numbers)) # get the max number

print(min(numbers)) # get the min number


# append functions
print("append functions")
numbers1 = [2,7,9,11,3]
numbers1.append(7)
print(numbers1)


# insert functions
print("insert functions")

numbers1.insert(1,67) # insert number into 1 index
print(numbers1)

# remove functions
print("remove functions")

numbers1.remove(9) # remove number 
print(numbers1)

numbers1.pop() #remove last element
print(numbers1)


numbers1[1] = 98
print(numbers1)

# Mutable = can change , List can change so that is mutable
# Inmutable = cannot change , Tuple cannot change so that is Inmutable

# List have [] square brackets
# Tuple have () parantheses brackets
# Disctonary have {} curly brackets

print("Tuple")
tp = (1,2,3)
tp = (1) # it means is not a tuple
tp = (1,) # it means is a tuple using comma at lat when tuple have only one element
print(tp)

# Swap two numbers 

# normal swaping using thirs variable

a=1
b=8

temp = a 
a= b
b=temp

print(a,b)

# swaping using Python
c=1
d=8
c,d=d,c

print(c,d)


