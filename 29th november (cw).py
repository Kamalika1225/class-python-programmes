class Employee:
    def __init__(self, name, Id, position):  
        self.name = name
        self.Id = Id
        self.position = position
    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nId: {self.Id}\nPosition: {self.position}")
class Address:
    def __init__(self, street, state, country):  
        self.street = street
        self.state = state
        self.country = country
    def displayAddressInfo(self):
        print(f"Street: {self.street}\nState: {self.state}\nCountry: {self.country}")
class EmployeeDetails(Employee, Address):
    def __init__(self, name, Id, position, street, state, country):
        Employee.__init__(self, name, Id, position)  
        Address.__init__(self, street, state, country)  
    def displayInfo(self):
        self.displayEmployeeInfo()  
        self.displayAddressInfo()  
obj = EmployeeDetails("kamalika", 100, "Manager", "KK Nagar", "TamilNadu", "India")
obj.displayInfo()
