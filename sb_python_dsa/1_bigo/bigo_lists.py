my_list = [11, 3, 23, 7]
my_list.append(17) #O(1)
my_list.pop() #O(1)
my_list.pop(0) # O(n) because you pop it from the start and have to move all the other indices
my_list.insert(0,11) #O(n)

# removing and adding is O(n)
# removing is only O(1) if it's at the end(no need to rearrange the other indices)
# searching by value is O(n), while searching by index to find the value is O(1)