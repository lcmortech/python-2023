##METHOD TO RETRIEVE DATA FROM LL

# def get(self, index):
#     if self.length == 0:
#         return None
#     self.head = Node(value)
#     self.tail

def get(self, index):
    if index < 0 or index >= self.length:
        return None
    temp = self.head

    for _ in range(index):
        temp = temp.next
    return temp
