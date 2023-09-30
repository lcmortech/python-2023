##METHOD FOR LINKED LIST
def print_list(self):
    #initiates temp at head of ll
    temp = self.head
    #while temp is not at the end of list
    while temp is not None:
        #print value for curr node
        print(temp.value)
        #move on to next node
        temp = temp.next 
