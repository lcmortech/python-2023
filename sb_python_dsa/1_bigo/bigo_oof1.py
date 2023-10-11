# As n gets bigger, the num of operations increases
# If n is 1, you have one operation and if n is a million, you still only have 1 operation.
# In the case of addition, you only have one operation
# O(1) is constant time
# Even if we have two additions, the num of operations will NOT increase but will remain constant
# It's the most efficient Big O

def add_items(n):
    return n + n + n