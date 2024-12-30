class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id=",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age,Id)
        self.Salary=Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary=",self.Salary)

man=Manager("Diana",35,100,20000)
man.displayManager()


#2
class Library:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print(f"Library Name: {self.name}")
class Member(Library):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
    def display_member_info(self):
        print(f"Member ID: {self.member_id}")
class Staff(Library):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id
        def display_staff_info(self):
            print(f"Staff ID: {self.staff_id}")

library = Library("Central Library")
member = Member("Central Library", "E24AI017")
staff = Staff("Central Library", "E24AI011")

print("Library Details:")
library.display_info()
print("\nMember Details:")
member.display_info()
member.display_member_info()
print("\nStaff Details:")
staff.display_info()
staff.display_staff_info()

