#  Dictonary Functions

#  Dictonary is nothing but it is a key value pairs

# denoted by {} curly brackets

# Dictonary is a Case sensitive

d1 = {}

print(type(d1))

d2 = {"kuldeep":"Math" , "amit":"science" , "sumit":"hindi" , "sachin":{"s1":"math","s2":"science","s3":"hindi"}}
d2["abhi"] = "computers"

del d2["abhi"]  # delete key from dictonary
print(d2)
print(d2["sachin"])


# Dictonary Functions

#  Copy functions
print("Copy functions")
print(d2.copy())

print(d2.get("kuldeep"))

print(d2.update({"deep":"programmer"}))   # line no 14 and update functions is same
print(d2)
print(d2.keys())
print(d2.items())
