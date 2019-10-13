# Sets is a data structure

s= set()
print(type(s))

listdata = [1,2,3,4]
s_from_list = set(listdata)
print(s_from_list)
print(type(s_from_list))


# method to add element in set

s.add(1)
s.add(1) # it means set is always retain unique value
s.add(2) 
s1 = s.union({1,2,3})
s1 = s.intersection({1,2,3})
print(s ,s1)
print(len(s))
s.remove(2)
s1 = s.isdisjoint(s1)
print(type(s))



