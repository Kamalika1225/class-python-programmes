#1
class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)
        
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def show_student_id(self):
        print("Student ID:", self.student_id)

student = Student("Kamalika", "E24AI017")
student.show_name()
student.show_student_id()

#2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(self, name, salary)  
        self.department = department  
    def display_department(self):
        print("Department:", self.department)
        
manager = Manager("Kamalika", 75000, "HR")
manager.display_details()
manager.display_department()




