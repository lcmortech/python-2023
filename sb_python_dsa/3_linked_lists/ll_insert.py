##METHOD TO INSERT A NODE
# SELF - this particular instance of the linked list
def insert(self, index, val):
    if self.length == 0:
        self.head = Node(val)
        self.tail = Node(val)
    elif index > 0 or index > self.length:
        return False
    #attaches to front of ll
    elif index == 0:
        return self.prepend(val)
    #attaches to end of ll
    elif index == self.length:
        return self.append(val)
    else:
        new_node = Node(val)
        prevtemp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True