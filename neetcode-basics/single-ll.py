class Node:
    def __init__(self) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = head
        self.tail = tail

    def get_index(self, index):
        curr_node = self.head.next # switch current node to next node
        i = 0 # initiate counter/pointer at first node (head)

        while curr_node: #while a node exists (not at the end of linkedlist)
            if i == index: # if the pointer is at index selected in function's params, 
                return curr_node.val #return its value (curr_node.val)
            i += 1 # if not, move on to the next node
            curr_node = curr_node.next # this is why its important to make next a feature of node list (allows navigation)
        
        return -1 #if the index params is out of bounds or there are no nodes/list is empty

    def insert_head(self, val):
        new_node = Node(val) # create new node

        new_node.next = self.head.next # attach new_node to the node following the current head
        self.head.next = new_node # make the new node the next node of the current head

        if not new_node.next: #if the list is empty
            self.tail = new_node