#  args and kwargs in python


# normal functions
def functions_name_print(a,b,c,d,e):
    print(a,b,c,d,e)

functions_name_print("ad","ae","we","wer","trt")


# args

def funargs(normal , *args):  #   arguments like always is first normal then after *args then **kwargs
    print(type(args))  # always tuple read in args
    print(normal)
    for item in args:
        print(item)

test = ["ad","ae","we","wer","trt"]    
valuetest = "this is test"
funargs(valuetest , *test)


# kwargs


def funargs(normal , *args , **kwargs):  #   arguments like always is first normal then after *args then **kwargs
    print(type(args))  # always tuple read in args
    print(normal)
    for item in args:
        print(item)
    print("kwargs")    
    for key,value in kwargs.items():
        print(f"{key} is a {value}")



test = ["ad","ae","we","wer","trt"]    
kw = {"math":"number","science":"string" , "history":"book"}
valuetest = "this is test"
funargs(valuetest , *test , **kw)