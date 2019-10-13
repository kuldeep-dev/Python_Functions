#  Loops in python

list1 = ["kuldeep","deep","amit","sumit","aman"]
list2 = [["kuldeep",1],["deep",2],["amit",3],["sumit",4],["aman",5]]

dict1 = dict(list2)   # change list to dict using dict type
print(dict1)
# print using for loop

# for loop using list
for item in list1:
    print(item)

for item , snumber in list2:
    print(item,"serial number is",snumber)   # it means iteration


# for loop using Dictonary

for item , snumber in dict1.items():
    print(item,"serial number is",snumber)   # it means iteration    


for item in dict1:
    print(item)


# Exercise

items = ["ints","floats","kuldeep",4,5,7,34,34,56,78,123,54,56,67,54]

for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)



# While loop

i = 0

while(i<10):
        # print(i)
        i = i+1


# break statement 

while(True):
        print(i+1,end="")
        if(i==10):
                break
        i+1        


while(True):
        if i+1<5:
                i = i+1
                continue # continue means continue the current iteration
        print(i+1,end=" ")
        if (i == 44):
                break   # break means exit the loop
        i = i+1        


# Exercise

print("Exercise")

while(True):
        i = int(input("Please Enter a number\n"))
        if(i<100):
                print("Try Again")
                continue
        else:
                print("You have entered a number greater than 100")
                break        



# making a faulty calculator

# taking input from the user and changing into integer
inp1 = input("Operator")

# taking 2nd input from user
inp2 = input("First number")

# taking 3rd number
inp3 = input("Last number")

# making a new variable
new_input = inp2 + inp1 + inp3

# checking the input
if new_input == "45*3":
    print(555)
elif new_input == "56+9":
    print(77)
elif new_input == "56/6":
    print(4)
elif inp1 == "*":
    print(int(inp2) * int(inp3))
elif inp1 == "+":
    print(int(inp2) + int(inp3))
elif inp1 == "-":
    print(int(inp2) - int(inp3))
elif inp1 == "/":
    print(int(inp2) / int(inp3))