# Pickle module in python 

import pickle

cars = ["maruti" , "bmw", "audi","test"]

# pickle the object in python

# file = "mycar.pkl"
# fileobj = open(file ,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# depickle means read pickle file

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)



# Exercise using iris dataset
# pickle
# Use requests module to download the iris dataset

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)

l2 =[item.split(",") for item in data.split("\n") if len(item)!=0]
# print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)


# To read this pickle file you can use this code
# import pickle
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))