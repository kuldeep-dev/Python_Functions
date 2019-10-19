#  Time module in python

#  get execution time python

import time

initial = time.time()
# print(initial)

for  i in range(45):
        print("Hello kuldeep")

print("For loop time",time.time() - initial,"seconds")



initial2 = time.time()

k =0
while (k<45):
        print("Hello kuldeep")
        k += 1

print("while loop time",time.time() - initial2,"seconds")



#  get current time 
localtime = time.asctime(time.localtime(time.time()))
print(localtime)


# sleep function

k =0
while (k<45):
        print("Hello kuldeep")
        time.sleep(2)   #hold time for two seconds
        k += 1