# Binary Search Tree Implementation in Python

# Create a node

class Node:
    def __init__ (self, key): # we are going to deal with keys, not vals
        self.key = key
        self.left = None
        self.right = None