#class that creates Node that each method in the ll class can call to create a new node
class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

    

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def __init__(self, value):
    #     #create new Node 
    # def append(self, value):
    #     #add Node to end
    # def prepend(self, value):
    #     #create new Node
    #     #add Node to beginning
    # def insert(self, index, value):
    #     #create new Node
    #     #insert Node

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)