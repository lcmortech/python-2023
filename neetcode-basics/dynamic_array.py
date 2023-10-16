#CONSTRUCT A DYNAMIC ARRAY
# Python lists are dynamic arrays by default
# This is an example of what goes on under the hood

class DynamicArray:
    def _init__(self, capacity, int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity
    
    #get value at a given index
    def get(self, i): 
        return self.arr[i]
    
    #set n at a given index:
    def set(self, i, n):
        self.arr[i] = n

    #insert n in the last position of the array    
    def insert(self, i, val): 
        if self.length == self.capacity:
            self.resize()
            
    # insert at next empty position
    def pushback(self, val): 
        if self.length == self.capacity:
            self.resize()

    def resize(self):
        pass
    def get_size(self):
        pass
    def get_capacity(self) -> int:
        return self.capacity
