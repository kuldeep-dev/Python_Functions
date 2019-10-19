# Raise in python 

# Built in exception

a = input("What is your name")
b = input("How much do you earn")

if b==0:
        raise ZeroDivisionError("B is zero so stop is programme")

if a.isnumeric():
        raise Exception("Numbers are not allowed")
print(f"hello {a}")

# value error

c = input("enter name")
try:
        print(a)

except Exception as e:
        if c=="kuldeep":
                raise ValueError("Kuldeep is not allowed")        
        print("variable not defined")        