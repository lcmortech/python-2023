#class that creates Node that each method in the ll class can call to create a new node
# None/null as the pointer of a node means it's the last node in the ll, or the "tail" of the ll
class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

    

class LinkedList:
    def __init__(self, value):
        #create new Node 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

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
    #     #add Node to beginning
    # def insert(self, index, value):
    #     #create new Node
    #     #insert Node

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)