# Pattern Printing
try:
    n = int(input("Enter No. of Row : "))
    b = int(input("Enter Pattern(0 or 1) : "))
    if b is 0:
        count = 0
        while(count<=n):
            print("*" * count, end="")
            print("\n", end="")
            count = count + 1
    elif b is 1:
        count = n
        while(count!=0):
            print("*" * count, end="")
            print("\n", end="")
            count = count - 1
    else:
        print("Invalied Pattern !!!")

except Exception as e:
    print("Invalied Input !!!")
