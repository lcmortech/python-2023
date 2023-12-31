# NOTES

# Design a singly linked list class. Your linkedlist class should support the following operations:


class Node: # Initializes an empty node with a val and next pointer
    def __init__(self) -> None:
        self.val = val
        self.next = None

class LinkedList: # Initializes an empty linked list
    def __init__(self):
        self.head = head
        self.tail = tail

    def get_index(self, index): # returns the value of the i-th note
        curr_node = self.head.next # switch current node to next node
        i = 0 # initiate counter/pointer at first node (head)

        while curr_node: #while a node exists (not at the end of linkedlist)
            if i == index: # if the pointer is at index selected in function's params, 
                return curr_node.val #return its value (curr_node.val)
            i += 1 # if not, move on to the next node
            curr_node = curr_node.next # this is why its important to make next a feature of node list (allows navigation)
        
        return -1 #if the index params is out of bounds or there are no nodes/list is empty

    def insert_head(self, val): # inserts a node with val at head
        new_node = Node(val) # create a new node

        new_node.next = self.head.next # attach new_node to the node following the current head
        self.head.next = new_node # make the new node the next node of the current head

        if not new_node.next: #if the list is empty
            self.tail = new_node
    
    def insert_tail(self, val): # inserts a node with val at tail
        self.tail.next = Node(val) # create a new node
        self.tail = self.tail.next

    def remove(self, index): # removes the i-th node
        pt = 0
        curr = self.head

        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next: # if curr node and a following node exist
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def get_values(self): # returns an array of all the vals in the list
        curr = self.head.next # initiate curr node, set to head.next
        res = [] # initiate empty list
        while curr: # while going thru the linkedlist,
            res.append(curr.val) # add the curr val of each node to res
            curr = curr.next # iterate to next node
        return res # else if listnode is empty, return empty res
