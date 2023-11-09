## NOTES

# Stacks - LIFO: Last In First Out

# Methods: Push, Pop, Peek

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = prev


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(None)

        self.length += 1
        if self.head is None:
            #new_node = self.head
            self.head = new_node
        
        new_node.prev = self.head
        self.head = new_node

    def pop(self):
        head = self.head
        self.head = head.prev

        return head.value


    def peek(self):
        return self.head.value


