#METHOD TO REMOVE AN ITEM IN LL

def remove(self, index, val):
    if index < 0 or index >= self.length:
        return None
    elif index == 0:
        return self.prepend()
    elif index == self.length - 1:
        return self.pop()
    prev = self.get(index - 1)
    temp = prev.next
    