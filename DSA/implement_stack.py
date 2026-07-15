#Implementing stack using lists and basic python 

MAX = 8
A = []

def pop():
    if len(A) == 0:
        print("Stack Underflow!!")
    else:   
        print(f"Popped an element {A[-1]}from A")
        A.pop()
        

def push():
    if len(A) == MAX:
        print("Stack Overflow!!")
    else:
        value = int(input("Enter value:"))
        A.append(value)
        print(f"{value} pushed into stack.")

def display():
    if len(A) == 0:
        print("Stack is empty")
    else:
        for i in range(len(A)-1,-1,-1):
            print("__")
            print(f"|{A[i]}|")
        print("__")

while True:
    print("\n---Stack Menu ---")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    
    choice = int(input("Enter your choice no. : "))

    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
