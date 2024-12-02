#1 
class Library:
    def __init__(self):
        self.books = ["Book1", "Book2", "Book3"]
    def show_books(self):
        print("Available books:", self.books)
        
class Member:
    def __init__(self, name):
        self.name = name
    def show_member(self):
        print("Member:", self.name)

class LibraryManagement(Library, Member):
    def __init__(self, name):
        Library.__init__(self)  
        Member.__init__(self, name)  
    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{self.name} borrowed {book_name}")
        else:
            print(f"{book_name} is not available")

member = LibraryManagement("kamalika")
member.show_member()
member.show_books()
member.borrow_book("Book1")
member.show_books()

#2
class Restaurant:
    def __init__(self):
        self.menu = {"briyani": 100, "Burger": 5, "Pasta": 8}
    def show_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")
            
class Delivery:
    def __init__(self, rider_name):
        self.rider_name = rider_name
    def show_rider(self):
        print("Delivery Rider:", self.rider_name)

class Order(Restaurant, Delivery):
    def __init__(self, rider_name, item):
        Restaurant.__init__(self)  
        Delivery.__init__(self, rider_name)  
        self.item = item

    def process_order(self):
        if self.item in self.menu:
            print(f"Order placed for {self.item}. Total: ${self.menu[self.item]}")
            print(f"Rider {self.rider_name} will deliver it.")
        else:
            print(f"{self.item} is not on the menu.")

order = Order("kamali", "briyani")
order.show_menu()
order.show_rider()
order.process_order()



