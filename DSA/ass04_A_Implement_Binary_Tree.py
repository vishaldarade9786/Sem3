class Node:
    def __init__(self,data):
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,"->" , end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data ,"->", end= ' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,"->",end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Operations
print("1.Inorder Traversal")
inorder(root)
print("\n")

print("2.Preorder Traversal")
preorder(root)
print("\n")

print("3.Postorder Traversal")
postorder(root)
print("\n")