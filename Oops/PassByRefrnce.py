class Customer :
    def __init__(self,name):
        self.name = name
    def greet(customer):
        print(id(customer))
        customer.name = "Reet"
        print(customer.name)
        print(id(customer))
    cust = Customer("Ram")
    print(id(cust))
    greet(cust)
    print(cust.name)
