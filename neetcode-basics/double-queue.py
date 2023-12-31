# NOTES

#A queque is known as a FIFO Data Structure (First In First Out (Queque))
#Unlike a single queue, with a double queue, you can add and take things from either end

# caught covid on mon (taking a break) (tues)
#covid day2 (wed)
#covid day3 (thurs)
#covid day4 (fri)
#covid day5 (sat)
#covid and christmas eve break (sun) (hope to feel better soon)
#covid break day6 and merry christmas! (mon)
#happy new year! (jan 1)

# Methods needed:
# push_back
# pop_back
# pop_front
# get_back
# get_front
# empty
# full 

# Alt Methods (simpler)
# insertFront()
# insertRear()
# deleteFront()
# deleteRear()

#Add Alt
# getFront()
# getRear()
# isEmpty()
# size()
# erase()


# Alternatively: Python has a built in double queue method: deque()

# from collections import deque

# my_deque = deque()

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

#class Deque:


    #def __init__(self):
       # self.head = self.tail = None

# Example from Pythonds:
class Deque:
    def __init__(self):
        self.items = [] # initiate stack

    def isEmpty(self):
        return self.items == [] # return stack if empty

    def addFront (self, item): # add item to stack
        self.items.append(item)
    
    def removeFront(self): # remove front item of stack
        return self.items.pop()

    def removeRear(self): # remove last item in stack
        return self.items.pop(0)

    def size (self): # returns the full size/length of the stack
        return len(self.items)

