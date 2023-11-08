## NOTES

# This is probably the most common data structure that I have implemented in many languages.
# FIFO - First In First Out (like waiting in line)
# To the whote board!
# We use a singly linked list, we don't need  a doubly linked list

# Runtime O(1) operations
# enqueue
# dequeue
# peek

# We're entering a world of DSA where constraints make things fast
# You will notice pretty much everything from here on out that what makes a lot of these data structures fast is the lack of features.

# CODE
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0
        # self.length = None
        # self.head = Node(None)
        # self.tail = None   

    def enqueue(self): #push
        new_node = Node(None)
        self.head = None

        if self.head is not None:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.head is None:
            return None
        self.length -= 1

        head = self.head
        self.head = self.head.next

        # free
        head.next = None

        return head.value

    def peek(self):
        return self.head.value