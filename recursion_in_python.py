# Recursions in python

# Resursion means use function in function

def print2(str1):
    print("This is " + str1)
print2("kuldeep")

print("factorial itrative method")
def factorial_itrative(n):
    """ 
    param n : integer
    return : n*n-1 * n-2 * n-3......1
    means n! : 5*4*3*2*1
    """
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
    

number = int(input("Enter the number"))
print(factorial_itrative(number))


# recursive method

def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)    

print(factorial_recursive(number))


# Fibonacci series

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)    

print(fibonacci(number))
