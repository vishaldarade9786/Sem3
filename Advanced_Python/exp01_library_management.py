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
        # The library just catches the book and puts it on the shelf.
        # No inputs, no prints. Pure logic.
        self.books.append(new_book)

    def register_patron(self, new_patron):
        # Hard lesson , This is only brain not ears and eyes or mouth.
        self.patrons.append(new_patron)

    def borrow_book(self,patron_id,target_book_id):
        # check if given values exist in database or not
        temp_patron,temp_book = None,None
        for el in self.patrons:
            if el.user_id == patron_id:
                temp_patron = el
                break
        for el  in self.books:
            if el.book_id == target_book_id:
                temp_book = el
                break

        if temp_patron == None:
            return "Error: Patron not found"
        elif temp_book == None:
            return "Error: Book not registered in library"
        elif temp_book.book_availability == False:
            return "Sorry, that book is already checked out"
        else:
            temp_patron.backpack.append(temp_book)
            temp_book.book_availability = False
            return "Book succesfully checked out"