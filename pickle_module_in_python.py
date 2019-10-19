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

