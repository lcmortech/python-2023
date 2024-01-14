# Binary Search Tree Implementation in Python (Programiz)

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

    # traverse right
    inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node is the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

# Find the inorder successor
def miniValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

        return current

# Deleting a node
def deletenode(root, key):

    # Return if key is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # If the node has two children,place the inorder successor in the node to be deleted
    temp = miniValueNode(root.right)

    # Delete the inorder successor
    root.right = deleteNode(root.right, temp.key)

return root



root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

# Test case
print("Inorder traversal", ends=' ')
