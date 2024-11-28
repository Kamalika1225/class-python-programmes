#1.
class Student:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        print(f"Student object created for {self.name}")

    def display(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")
        
    def __del__(self):
        print(f"Student object for {self.name} is being deleted.")
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
course = input("Enter student's course: ")
grade = input("Enter student's grade: ")
student = Student(name, age, course, grade)
student.display()

del student


#2
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        percentage = sum(self.marks) / 3
        if percentage >= 85:
            return "S"
        elif percentage >= 75:
            return "A"
        elif percentage >= 65:
            return "B"
        elif percentage >= 55:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "Fail"

    def display(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")

name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
marks = [float(input(f"Enter marks for subject {i+1}: "))for i in range(3)]

student = Student(name, roll_number, marks)
student.display()

