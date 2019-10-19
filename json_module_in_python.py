# Json module in python  Json is Javasecript object notation

import json

data = '{"var":"kuldeep","var2":56}'

# json parse in python using json.loads
parsed = json.loads(data)
print(parsed['var'])

# json.dump change dictonary to json
data2 = {  # this is dictionary
    "name" : "kuldeep",
    "sujects" : ['math','science','english'],
    "company" : ('infy','tcs','apple','google'),
    "isbad" : False
}

jscomp = json.dumps(data2)
print(jscomp)
