# NOTES

#A queque is known as a FIFO Data Structure (First In First Out (Queque))
#Unlike a single queue, with a double queue, you can end and take things from either end

# caught covid (taking a break)
#covid day2
#covid day3

# Methods needed:
# push_back
# pop_back
# pop_front
# get_back
# get_front
# empty
# full 

# Alternatively: Python has a built in double queue method: deque()

# from collections import deque

# my_deque = deque()

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

class Dequeue:
    def __init__(self):
        self.head = self.tail = None

