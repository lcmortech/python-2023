## POP METHOD
#High-Level Overview
# We need tail to point to something that is pointing to the node before, and before that, and so on
# Set tail pointer to that pointer
# Then set tail.next equal to None
# Return the node popped at the end of the list

#Bring in two variables pre and temp and set them equal to head
# Remove head and tail for now
#If temp.next is equal to not None (not at the end of the list)
# Set pre equal to temp (already in the first iteration)
# Set temp to temp.next
# Remove temp and work with pre variable
# Then set tail equal to pre
# Set tail.next to None
# Return temp

# CODE

def pop(self):
    #edge case 1
    if self.length == 0: #if head is None and tail is None (there is nothing in the list)
        return None
    #orwhile temp.next is not None, if temp is pointing to a node its true until the end of the list when it isnt pointing to anything
    while(temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre #only used here
    self.tail.next = None #breaks the last node off 
    self.length =-1 #decrements to next node (subtracts = pop)
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp