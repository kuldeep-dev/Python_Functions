# Request for htttp module

import requests

#  GET request
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# POST request

url = "test.com"
data = {
    "p1" : 2,
    "p2" : 3,
    "p3" : 4
}
r2 = requests.post(url=url,data=data)