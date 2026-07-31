MAX_CAPACITY =  10
class TicketCounter:
    def __init__(self):
        self.line = [None]*MAX_CAPACITY
        self.front = -1 
        self.rear = -1
    # Enqueue Operation
    def enqueue(self,customer):
        if self.rear == MAX_CAPACITY - 1:
            return f"The Queue is already full."
        else:
            self.rear += 1 
            if self.front == -1 : self.front = 0
            self.line[self.rear] = customer
            return f"{customer} Enqueued Successfully."
    # Dequeue Operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            return f"The Queue is empty."
        else:
            customer = self.line[self.front]
            self.front += 1
            return f"{customer} Dequeued Successfully."
    # Peek Operation 
    def peek(self):
        if self.front == -1 or self.front > self.rear:
            return f"The Queue is empty."
        else:
            return f"{self.line[self.front]} is the First element to peek."
    # Display Operation
    def display(self):
        if self.front == -1 or self.front > self.rear:
            return f"The Queue is empty."
        else: 
            Queue = "Queue: "
            for i in range(self.front,self.rear+1):
                Queue += f"[{self.line[i]}] "
            return Queue

counter = TicketCounter()
if __name__ == "__main__":
    while True:
        try:
            choice = int(input("\n--- Ticket Booking Counter---\n1. Add Customer to Line(Enqueue)\n2. Serve Next Customer(Dequeue)\n3. Check Next Customer(Peek)\n4. Display Line\n5. Exit\nEnter Your Choice(1-5): "))
            if choice == 1:
                name = input("Enter customer name: ")
                print(counter.enqueue(name))
            elif choice == 2:
                print(counter.dequeue())
            elif choice == 3:
                print(counter.peek())
            elif choice == 4:
                print(counter.display())
            elif choice == 5:
                print("Exiting the Program.")
                break
        except ValueError:
            print("Enter valid value between 1-5.")
            