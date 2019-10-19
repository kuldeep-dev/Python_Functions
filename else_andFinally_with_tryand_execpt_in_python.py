#  Else and Finally with try and Execpt in python 

f1 = open("test.txt")

try:
        f = open("does.txt")

except Exception as e:
        print(e)

except EOFError as e:
        print("EOF error")

except IOError as e:
        print("io error")

else:  # except aur else me se sirf ek run hogi except ya phir else
        print("this will run only if except is not running")

finally: # finally tb use krte h jb error aaye to b code run krna ho kuch
        print("run this any way")        
        # f.close()
        f1.close()

print("Important stuff")