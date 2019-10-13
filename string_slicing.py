#  string slicing in python

mystr = "computer is a machine"

print(len(mystr)) #string length

print(mystr[0:4]) #string slicing


#  2 means 1 character miss krega
#  3 means 2 character miss krega
print(mystr[0:7:2]) #skip 2 character

print(mystr[0:]) #legth character tk le lega 0 to last

print(mystr[:5]) # start 0 se krega 

print(mystr[::]) # all character aa jeyenge as same print(mystr[0:7:1])


# using negative number
print("Negative number")
print(mystr[-1:]) # it means reverse the string  start with last character -1 ,-2,-3
print(mystr[-4:-2])
print(mystr[::-1]) #reverse the string


#  some string functions
print("some string functions")

print(mystr.isalnum())  # return boolean value true,false check isalfanumeric 

print(mystr.isalpha()) # return boolean value true,false check isalfa

print(mystr.endswith("machine")) # check at the end of string

print(mystr.count("c")) # count the existing character

print(mystr.capitalize()) # this function capital the first character

print(mystr.find("is")) # this function find the character in string

print(mystr.lower()) # convert string into lower case

print(mystr.upper()) # convert string into upper case

print(mystr.replace("is", "are")) # this function replace the is with are