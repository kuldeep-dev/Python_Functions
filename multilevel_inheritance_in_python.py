# Multilevel Inheritance in opps using python

class Dad:
    basketball =1
    

class Son(Dad):
    dance = 1
    basketball =9
    def isdance(self):
        return f"Yes I dance {self.dance} no of items"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Yes I dance very awesome {self.dance} no of items"


darry = Dad()
kuldeep = Son()
amit = Grandson()

print(amit.isdance())
print(amit.basketball)