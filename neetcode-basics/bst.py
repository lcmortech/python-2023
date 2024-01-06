# Binary Search Tree Implementation in Python

# Create a node

class Node:
    def __init__ (self, key): # we are going to deal with keys, not vals
        self.key = key
        self.left = None
        self.right = None

# inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left) # traverse left

    if root is None: # return if tree is empty
        return root

    # traverse root
    print(str(root.key) + "->", end= ' ')
    