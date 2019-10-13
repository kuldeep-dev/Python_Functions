#  File read and write in python

"""

"r"  - Open file for Reading -- Default mode
"w"  - Open file for writing 
"x"  - Creates file if not exists
"a"  - Add more contect to a file
"t"  - Text mode (Open as a text file) -- Default mode
"b"  - Binary mode
"+"  - Read and write 

"""


# File Reading

print("File Reading")

f = open("file.txt","r")
content = f.read()
print(content)
f.close()

# "b"  - Binary mode
print("Binary mode")
f = open("file.txt","rb")
content = f.read()
print(content)
f.close()


# "t"  - Text mode (Open as a text file) -- Default mode
print("Text mode")
f = open("file.txt","rt")
content = f.read(3) # read first three character
print(content)

content = f.read(3) # read after three character
print(content)
f.close()


# Read contect line by line

f = open("file.txt","rt")
# content = f.read() 
for line in f:
    print(line,end="")


# Readline function
f = open("file.txt","rt")
print(f.readline()) # it read only one line in one time
print(f.readline())


# Readlines functin store data in list
f = open("file.txt","rt")
print(f.readlines())




# File Writing

print("File Writing")

#  in this function add the new data in file every time delete all data and write new data
f = open("file.txt","w")
f.write("new line added")
f.close()


# add new line without delte the existing data
# "a"  - Add more contect to a file

f = open("file.txt","a")
f.write("new line added\n")
f.close()

# return number of character write in file

f = open("file.txt","a")
a = f.write("new line added\n")
print(a)
f.close()


# "+"  - Read and write 
# handle read and write both

f = open("file.txt", "r+") 
print(f.read())
f.write("new thanks")
f.close()


# tells the file pointer is in the file 
print("tell function")
f = open("file.txt")
print(f.tell())  # tells the file pointer is in the file 
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()


print("seek function")
f = open("file.txt")
print(f.readline())
f.seek(0) # seek means reset the file pointer and tell stating point of the pointer that means f.seek(10)
print(f.readline())
f.close()


#  How to open file using with Block

print("How to open file using Block")

with open("file.txt") as f:
    a = f.read(4)
    print(a)




