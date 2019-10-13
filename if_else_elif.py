# if and else condition

var1 = 6
var2 = 56
# var3 = int(input())

# if var3 >var2:
#     print("Greater")
# elif var3 == var2: #else if used as elif in python
#     print("Equal")    
# else:
#     print("Lesser")


# in keyword
# not in keyword

list1 = [5,7,3]
if 5 in list1:
    print("yes it in the list")


if 15 not in list1:
    print("no it not the list")



# Short hand if else 

a = int(input("Enter a\n"))
b = int(input("Enter b\n"))


if a>b: print("a is greater")



# Excercise

n = 18

print("\t \t \t \t Guessing Game \n")

no_guess = 0
no_try = 5

print("You have 5 chances \n")


while(no_guess < no_try):

    Guess = int(input("Guess the no:"))


    if Guess == n:
        print("You won this game in the" , no_guess + 1,"chance" )
        break

    if Guess > 30:
        print("Write the number smaller than 30 \n")

    elif(Guess <= 10):
        print("Increase your number")

    elif(Guess >= 19):
        print("Decrease your number")

    elif (Guess >= 10 and Guess < n) :
        print("Little increase your number")

    else:
        print("Your number is decimal or a negative integer ")


    print("Guess:",no_guess + 1,"\n")

    no_guess = no_guess + 1



# Excercise 2

a = int(input("Please add number of line you print"))
b = bool(int(input("Please enter 0 or 1")))

def start(a,b):
    if b == True:
        c = 1
        while c<=a:
            print(c*"*")
            c = c+1
    else:
        while a> 0:
            print(a * "*")
            a = a-1

start(a,b)                    
