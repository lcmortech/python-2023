## POP OFF FIRST NODE IN LL METHOD

# def popfirst(self, value):
#     if self.length == 0:
#         self.head = 

def popfirst(self, value):
    if self.length == 0: #if there's no node to pop off
        return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
        self.tail = None
    return temp