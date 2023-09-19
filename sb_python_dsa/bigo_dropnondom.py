# Drop the non-dominant constant

def print(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            # O(n^2)

    for k in range(n):
        print(k)
        #O(n)

# O(n^2) + O(n) = O(n^2 + n)
# When it comes to num of operations, even if it's just 100 operations, O(n^2) will be 10,000 while O(n) will only be 100.
# This makes n^2 dominant over n operations. Since n is non-dominant, we can just drop it.
# This leaves us with O(n^2)