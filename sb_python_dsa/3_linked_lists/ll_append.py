##APPEND METHOD FOR LINKEDLIST CLASS
# Edge cases come first

def append(self, value):
    new_node = Node(value)

    #Edge cases come first
    if self.head is None: #No node is present
        self.head = new_node
        self.tail = new_node
    else:
        #set tail(pointer) and the last node(value) both to the new node
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1
    # For a later method that requires the use of append and a boolean value to be returned
    return True

# def append(self, value):
#     if head.next is None:
#         head = next
#         tail = next
    
#     else:
#         prev.node = next
#         tail = next