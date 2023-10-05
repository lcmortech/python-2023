## PREPEND METHOD FOR LINKED LIST
# Adds an item to the beginning of the linked list
# set the next pointer on that node equal to something pointing at that node (head)
# then we have head point to the new node in the list
# In an empty list we have head and tail point to the new node

def prepend(self, value):
    new_node = Node(value)

    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    
    else:
        new_node.next = self.head
        self.head = new_node
    
    self.length += 1
    return True #optional