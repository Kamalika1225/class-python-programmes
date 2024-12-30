class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def validatedetails(self):
        if not (self.student_id.startswith('STU') and len(self.student_id) == 7):
            return "Invalid student ID"
        if len(self.name) < 2 or not all(x.isalpha() or x.isspace() for x in self.name):
            return "Invalid name"
        valid_grades = [f"{i}th Grade" for i in range(1, 13)]
        if self.grade not in valid_grades:
            return "Invalid grade"
        return "All details are valid"

    def display_details(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nGrade: {self.grade}"

student = Student("STU1234", "kamalika", "10th Grade")
print(student.validatedetails())
print(student.display_details())
