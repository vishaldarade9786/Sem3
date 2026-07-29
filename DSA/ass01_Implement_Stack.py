class BookStack:
    def __init__(self):
        # The stack is just a standard Python list
        self.stack = []

    def push(self, book_title):
        """Return Book: Adds a book to the top of the stack."""
        self.stack.append(book_title)
        return f"'{book_title}' returned and placed on top of the stack."

    def pop(self):
        """Arrange Book: Removes and returns the top book for shelving."""
        # Guard clause: check if the stack is empty first
        if len(self.stack) == 0:
            return "Error: The stack is empty. No books to arrange."
        
        # .pop() automatically removes the last item in a list
        shelved_book = self.stack.pop()
        return f"'{shelved_book}' taken from the top to be shelved."

    def peek(self):
        """Top Book: Looks at the top book without removing it."""
        if len(self.stack) == 0:
            return "The stack is empty."
        
        # Index -1 always grabs the very last item in a Python list
        top_book = self.stack[-1]
        return f"The book currently on top is '{top_book}'."

    def display(self):
        """Display Stack: Shows all books from top to bottom."""
        if len(self.stack) == 0:
            return "The stack is currently empty."
        
        print("\n--- Current Return Stack (Top to Bottom) ---")
        # Loop through the list backwards so the 'top' prints first
        for book in reversed(self.stack):
            print(f"- {book}")
        print("--------------------------------------------")
        return "" # Returning empty string keeps the CLI print clean


# --- Terminal UI (Mouth and Ears) ---
if __name__ == "__main__":
    library_desk = BookStack()
    
    while True:
        print("\nLibrary Return Desk")
        print("1. Return Book (Push)")
        print("2. Arrange Book (Pop)")
        print("3. Check Top Book (Peek)")
        print("4. Display Stack")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                title = input("Enter the title of the returned book: ")
                print(library_desk.push(title))
                
            elif choice == 2:
                print(library_desk.pop())
                
            elif choice == 3:
                print(library_desk.peek())
                
            elif choice == 4:
                # The display method handles its own printing formatting
                library_desk.display()
                
            elif choice == 5:
                print("Closing the return desk. Goodbye!")
                break
                
            else:
                print("Error: Please select a valid number from 1 to 5.")
                
        except ValueError:
            print("Error: Invalid input. Please enter a number.")