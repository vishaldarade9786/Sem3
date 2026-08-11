class Node:
    def __init__(self,data):
        self.data = data
        self.next: "Node | None" = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None  
    def addFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
    def addLast(self,value):
        node = Node(value)
        if self.head is not None:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = node
        else:
            self.head = node
    def insert(self,value,position):
        if position == 0:
            self.addFirst(value)
        elif position == -1:
            self.addLast(value)
        else:
            current_position = 0
            temp_node = self.head
            node = Node(value)
            while current_position < position-1:
                current_position += 1
                if temp_node.next is None:
                    break
                temp_node = temp_node.next
            node.next = temp_node.next
            temp_node.next = node
    def display(self):
        ans = []
        pointer = self.head
        while pointer is not None:
            ans.append(str(pointer.data))
            pointer = pointer.next
        return '=>'.join(ans)

