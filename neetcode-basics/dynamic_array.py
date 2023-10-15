#CONSTRUCT A DYNAMIC ARRAY
# Python lists are dynamic arrays by default


class DynamicArray:
    def _init__(self, capacity, int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity
    
    def get(self, i): 
        return self.arr[i]
    
    def insert(self, i, val): 
        pass
    def pushback(self, val): 
        if self.length == self.capacity:
            self.resize()

    def resize(self):
        pass
    def get_size(self):
        pass
    def get_capacity(self) -> int:
        return self.capacity
