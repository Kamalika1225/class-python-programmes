#1
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployee()
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()


#2
class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID:",self.prodId)
        print("Product Name:",self.prodName)
        print("Product Count:",self.prodCount)
obj=Inventory("E24AI017","blue heaven",5)
obj.display()

#3
class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID=",self.prodId)
        print("Product Name=",self.prodName)
        print("Product Count=",self.prodCount)
class Todisplay(Inventory):
    def getdet(self):
        self.display()
obj=Todisplay("E24AI017","blue heaven",5)
obj.getdet()


