##METHOD FOR SETTING THE VALUE

def set_value(self, index, val):
    temp = self.get(index)
    #if temp is NOT None
    if temp:
        temp.value = val
        return True
    return False  
