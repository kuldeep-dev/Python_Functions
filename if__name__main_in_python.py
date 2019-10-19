# if __name__ == __main__ usages  in python


def printkul(str):
    return f"this is test string {str}"


def add(num1,num2):
    return num1 + num2 +5

# print("and the name is", __name__)

if __name__ == "__main__":
    print(printkul("kuldeep"))
    o = add(3,4)
    print(o)