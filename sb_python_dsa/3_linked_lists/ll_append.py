##APPEND METHOD FOR LINKEDLIST CLASS
# Edge cases come first
# Self refers to the linked list itself

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


##ALT

def append_2(self, value):
    new_node = Node(value)

    if self.length == 0:
        self.head = new_node
        self.tail = new_node

    else:
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1
    return True

# def append(self, value):
#     if head.next is None:
#         head = next
#         tail = next
    
#     else:
#         prev.node = next
#         tail = next