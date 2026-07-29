MAX = 5
class Queue:
    def __init__(self):
        self.queue = [None]* MAX
        self.rear = -1
        self.front = -1    
    def enqueue(self,item):
        if self.rear == MAX-1:
            return f'Queue is full'
        else:
            self.rear +=1
            if self.front == -1: self.front = 0
            self.queue[self.rear] = item
            return f'{item} Enqueued Successfully.'
    
    def display(self):
        for i in range(self.front,self.front+1):
            return i

    def dequeue(self):
        if self.front > self.rear:
            return("Queue is empty.")
        else:
            self.front += 1 
            return f'item dequeued succesfully.'
    
    def peek(self):
        if self.front > self.rear:
            return("Queue is empty.")
        else:
            return f'first Item is{self.queue[self.front]}'

my_queue =Queue()

while True:
    try:
        choice = int(input("Choose the sr.no. To perform an action.\n1.Enqueue\n2.Display\n3.Dequeue\n4.Peek\n5.Exit\nYour choice :"))

        if choice == 1:
            item = input("Enter the item you want to Enqueue:")
            print(my_queue.enqueue(item))
        elif choice == 2:
            print(my_queue.display())
        elif choice == 3:
            print(my_queue.dequeue())
        elif choice == 4:
            print(my_queue.peek())
        elif choice == 5:
            print("Exiting the Program!")
            break
    except ValueError:
        print("Please Enter valid integer values for choices.")