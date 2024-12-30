class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp=Employee("hari",20000000)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)




class Student:
    def __init__(self,name,rollno):
        self.__name=name
        self.rollno=rollno
    def display(self):
        print("Name:",self.__name)
        print("Rollno:",self.rollno)
s=Student("kamali","E24AI017")
s.display()
print(s.name)


class Student:
    id=123
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
s=Student("Kamalika")
s.display()
print(s.id)


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp=Employee("hari",20000000)
print("Name:",emp.name)
print("Salary:",emp._Employee_salary)
