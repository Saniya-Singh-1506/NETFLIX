class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#inorder = left-root-right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data , end=" ")
        inorder(root.right)
        
#preorder = root-left-right

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
        
# Postorder = left → right → root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

        
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)


print("Inorder Traversal:")
inorder(root)       # Output: 4 2 5 1 3

print("\nPreorder Traversal:")
preorder(root)      # Output: 1 2 4 5 3

print("\nPostorder Traversal:")
postorder(root)     # Output: 4 5 2 3 1

        
            
    
    
        