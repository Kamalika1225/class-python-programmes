#1. 
class User:
    def __init__(self, username, password):
        self.__username = username
        self.set__password(password)

    def set__password(self, password):
        if len(password) < 8:
           print("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
        if not any(char in "!@#$%^&*()-_+=<>?/\\|~" for char in password):
            print("Password must contain at least one special character.")
        self._password = password
        
    def check_password(self, input_password):
        return self._password == input_password

user = User("kamalika", "Lotus1225@")
print(user.check_password("Lotus1225@"))


#2. 
class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self.set_price(price)
        self.set_stock(stock)

    def set_price(self, price):
        if price <= 0:
            print("Price must be greater than 0.")
        self._price = price

    def set_stock(self, stock):
        stock = int(stock)
        if stock < 0:
            print("Stock must be a non-negative integer.")
        self._stock = stock

    def get_stock(self):
        return self._stock

product = Product("Laptop", 1500, 10)
product.set_price(2000)
product.set_stock(20)
print(product.get_stock())


#3.   
class Student:
    def __init__(self, name, age, marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if age < 5 or age > 100:
            print("Age must be between 5 and 100.")
        self._age = age

    def get_age(self):
        return self._age

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
        self._marks = marks

    def get_marks(self):
        return self._marks

student = Student("Alice", 20, 85)
student.set_age(21)
print(student.get_marks())













