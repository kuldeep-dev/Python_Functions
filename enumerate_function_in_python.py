#  Enumerate functions

l1 = ["math","science","hindi","python","computer"]

i =1
for item in l1:
        if i%2 is not 0:
                print(f"please subjects choose {item}")
        i +=1



# Enumerate function 

# Enumerate function return index and item
print("Enumerate function")

for  index,item1 in enumerate(l1):
        if index%2 == 0:
                print(f"please subjects choose {item1}")
