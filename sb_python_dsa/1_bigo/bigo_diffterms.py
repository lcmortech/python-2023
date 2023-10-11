# Diff terms for inputs
def print_items(a, b):
    for i in range(a):
        print(i)
        # O(a)
    for j in range(b):
        print(j)
        # O(b)

# You can't drop or simplify diff constants/parameters
# becomes O(a + b)
        
print_items(10)

# Diff terms for inputs
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(j)
            # O(a * b)