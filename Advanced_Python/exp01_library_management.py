class Book:
    def __init__(self,title,book_id,book_availability = True):
        self.title=title
        self.book_id = book_id
        self.book_availability = book_availability
    

class Patron:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        # Every new patron gets their own empty list
        self.backpack = []

class Library:
    def __init__(self):
        # The Library acts as the central database
        self.books = []
        self.patrons = []

    def add_book(self, new_book):
        # Creating a Book
        new_book = Book(input("Enter the title of book:"),int(input('Enter book_id :')))
        # Adding the book to database
        self.books.append(new_book)

    def register_patron(self, new_patron):
        # Creating a Patron
        new_patron = Patron(input("Enter Name :"),int(input("Enter user id :")))
        # Adding the Patron to database
        self.patrons.append(new_patron)