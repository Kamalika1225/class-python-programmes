#1.
class BankAccount:
    def _init_(self,holder_name,account_no,balance):
        self.holder_name=holder_name
        self.account_no=account_no
        self.balance=balance
    def deposit_money(self,amount):
        if amount>0:
            self.balance+=amount
            print("The amount after deposited :",self.balance)
    def withdraw_money(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("The amount after withdraw :",self.balance)
        else:
            print("The account balance is insufficient to withdraw the money")
            
    def display(self):
        print("Account Holder Name:",self.holder_name)
        print("Account Number:",self.account_no)
        print("Balance amount in your Account:",self.balance)
obj1=BankAccount("Harini Raja","24350687910",3000)
obj1.display()
obj1.deposit_money(10000)
obj1.withdraw_money(10000)

#2. 
class Cosmetics:
    def __init__(self,name="kajal",brand="lakme",price=120,category="eye makeup"):
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category
    def display(self):
        print("Cosmetic Product Information:")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")
obj=Cosmetics("lip stick","blue heaven",200,"lip care")
obj.display()


