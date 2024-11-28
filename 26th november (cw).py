#1.
class Book:
    def _init_(self,bookname,author):
        self.bookname=bookname
        self.author=author
    def display(self):
        print("The name of the Book:",self.bookname)
        print("The name of the Author:",self.author)
obj1=Book("The pie","Leo Tolstoy")
obj1.display()

#2.
class Book:
    def _init_(self):
        self.bookname="The pie"
        self.author="Leo Tolstoy"
    def display(self):
        print("The name of the Book:",self.bookname)
        print("The name of the Author:",self.author)
obj1=Book()
obj1.display()

#3.
class Book:
    def _init_(self,library,bookname="The pie",author="Leo Tolstoy"):
        self.library=library
        self.bookname=bookname
        self.author=author
    def display(self):
        print("The name of the library:",self.library)
        print("The name of the Book:",self.bookname)
        print("The name of the Author:",self.author)
obj1=Book("e-library")
obj1.display()

        
