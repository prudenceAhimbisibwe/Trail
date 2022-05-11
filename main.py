
class Customer:
    def __init__(self,name,city,country):
        self.name=name
        self.city=city
        self.country=country
customers=[
    Customer("Neverce","Kampala","Uganda"),
    Customer("susan","Nairobi","Kenya"),
    Customer("Lillian","kigali","Rwanda"),
    Customer("John","Nairobi","Kenya"),
    Customer("Jane","Kampala","Uganda"),  
]
for c in customers:
    print(f"{c.name},{c.city},{c.country}")
    customers[1].verified=False
    print(customers[1].verified)