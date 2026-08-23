class BookNode:
    def __init__(self,title):
        self.left = None
        self.right = None
        self.book_title = title

def inorder(root):
    if root:
        inorder(root.left)
        print(root.book_title,"->",end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.book_title,"->",end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.book_title,"->",end=' ')


# Creating and storing Nodes for Tree
root = BookNode("Primary School")
root.left = BookNode("Class1")
root.right = BookNode("Class2")
root.left.left = BookNode("Class1-Math")
root.left.right = BookNode("Class1-Science")
root.right.left = BookNode("Class2-Math")
root.right.right = BookNode("Class2-Science")

# Operations Performed
print("1.Inorder")
inorder(root)
print("\n")

print("2.Preorder")
preorder(root)
print("\n")

print("3.Postorder")
postorder(root)
print("\n")