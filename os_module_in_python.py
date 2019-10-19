# Os module in python

import os 

 print(dir(os))


print(os.getcwd())  #getced means get current working directory

 os.chdir("c:\\") # change the working directory
 print(os.getcwd()) 


# List dir
print(os.listdir()) # return all files and folders currently stored in working directory
# print(os.listdir("c:\\")) # return all files and folders that path "c:\\" 

# create folder 
os.mkdir("thistest") # create folder in current directory
os.makedirs("this/that") # create multiple directories 
os.rename("kuldeep.txt","sandeep.txt") # rename file name kuldeep.txt to sandeep.txt

# Read enviornment variable

print(os.environ.get('HOME'))  # get enviornment valriable

# join

os.path.join("C:\\","kuldeep.txt")  # join the two path 

os.path.exists("c:\\")  # this path exist or not return true or false

os.path.isfile("c:\\kuldeep.txt") # isfile return file is exist or not
os.path.isdir("c:\\kuldeep") # isdir return directory is exist or not
