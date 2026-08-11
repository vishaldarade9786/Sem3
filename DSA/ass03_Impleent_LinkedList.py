class Node:
    def __init__(self,data):
        self.data = data
        self.next: 'Node | None' = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None  
    def addFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def display(self):
        if self.head is None:
            return f"The Linked List is Empty"
        else:
            ans = []
            pointer = self.head
            while pointer is not None:
                ans.append(str(pointer.data))
                pointer = pointer.next
            ans.append("NULL")
            return '=>'.join(ans)


if __name__ == "__main__":
    library_books = Singly_Linked_List()
    while True:
        print("\n--- Library Book ID Manager ---")
        print("1.Insert at the Beginning")
        print("2.Display")
        print("3.exit")
        try:
            choice = int(input("Enter your choice here :"))
            if choice == 1:
                val = input("Enter the value you want to Enter : ")
                library_books.addFirst(val)
                print(f"Value added Successfully")
            elif choice == 2:
                print("Linked List -->")
                print(library_books.display())
            elif choice == 3:
                print("Exiting Gracefully")
                break
            else:
                print("Enter valid Choice between 1-3")
        except ValueError:
            print("Enter Valid value")