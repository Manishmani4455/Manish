#Recursive python program for level
#order teaversal of binary tree
class Node:
    # A utitity function to create a new node
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

# Function to print Level Order traversal of tree
    def PrintLevelOrder(Root):
        h=height(Root)
        for i in range(1,h+1):
            printCurrentLevel(root,i)

# Print node at a current level
    def PrintCurrentLevel(root,level):
        if root is None:
            return
        if level==1:
            print(root.data,end="")
        elif level>1:
            printCurrentLevel(root.left,level-1)
            printCurrentLevel(root.right,level-1)
    def height(node):
        if node is None:
            return 0
        else:
            # Computer the height of each subtree
            lheight=height(node.left)
            rheight=height(node.right)

# Use the larger one
        if lheight>rheight:
            return lheight+1

        else:
            return rheight+1

#Driver program to test above function
Root=Node(1)
Root.left=Node(2)
Root.right=Node(3)
Root.left.left=Node(4)
Root.left.right=Node(5)
Root.right.left=Node(6)
Root.right.right=Node(7)
print("Level order traversal of binary tree is")
PrintLevelOrder(Root)
