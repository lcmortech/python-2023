# SEGMENT TREE DATA STRUCTURE (Geek4Geeks)

# A Segment Tree is a data structure that allows programmers to solve range queries over the given array effectively and to modifying the array values. Basically, Segment Tree is a very flexible and efficient data structure and a large number of problems can be solved with the help of segment trees.

# Representation of Segment trees 
# Leaf Nodes are the elements of the input array. 
# Each internal node represents some merging of the leaf nodes. The merging may be different for different problems. For this problem, merging is sum of leaf nodes under a node.
# An array representation of tree is used to represent Segment Trees. 

# For each node at index i, the left child is at index (2*i+1), right child at (2*i+2) and the parent is at  (⌊(i – 1) / 2⌋).

#Construction of Segment Tree from the given array:
# We start with a segment arr[0 . . . n-1]. and every time we divide the current segment into two (if it has not yet become a segment of length 1), and then call the same procedure on both halves, and for each such segment, we store the sum in the corresponding node. All levels of the constructed segment tree will be completely filled except the last level. Also, the tree will be a Full Binary Tree because we always divide segment in two, at every level. Since the constructed tree is always a full binary tree with n leaves, there will be n-1 internal nodes. So the total number of nodes will be 2*n – 1.

# What is the height of a segment tree of a given array?

# Height of the segment tree will be ⌈log₂N⌉. Since the tree is represented using array and relation between parent and child indexes must be maintained, size of memory allocated for segment tree will be (2 * 2⌈log2n⌉  – 1).

# Query for sum of a given range

# Once the tree is constructed, we need to get the sum using the constructed segment tree.

# Implementation (CodeSpeedy)

# function to build the segmenttree array
def buildTree(a):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = a[i]

    # creating parent node by adding left and right child
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]

# function to update a node of the tree
def updateTree(index, value):
    # set value at position index 
    tree[index + n] = value
    index+=n

    # after updating the child node,update parents
    i = index

    while i > 1: 
    #update parent by adding new left and right child
        tree[i//2] = tree[i] + tree[i^1]
        i =i//2

#function to find sum on different range 
def queryTree(l, r):
    sum = 0

    #to find the sum in the range [l,r)
    l += n
    r += n

    while l < r:

        if ((l & 1)>0):
            sum += tree[l]
            l += 1

        if ((r & 1)>0):
            r -= 1
            sum += tree[r]

        l =l// 2
        r =r// 2

    return sum

# To check these three non-recursive functions, we have to write the main function:
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7,8]
    n = len(A)
    buildTree(A)
    print(queryTree(1, 4))
    updateTree(2, 5)
    print(queryTree(1, 4))

# Output
# // 9
# // 11

# Final Notes
# Segment Tree is basically a data structure. It can be used to perform range queries and updates in an easy and fastest way.
# To understand Segment Tree we have to take an array first.
# Let’s take an array A=[1,3,5,6,7,-3,6,2] of length 8 indexed from 0 to 7 and we have to solve problems called range queries and updates.
# 1. Range queries mean to determine the sum of different segments of the given array. Example-sum(0,3)=1+3+5+6=15  (Here 0 and 3 represent the index no. of the given array).
# 2. update means to change the value of a specified element of the given array to a new value. Example-If we perform an update(3,5), then the array becomes A=[1,3,5,5,7,-3,6,2] (Here 3 represents the index of the array, whose value to be changed and 5 represent the new or updated value).
# 3. After performing the update, the sum(0,3) becomes 14(1+3+5+5) because of updating the value of the element index 3.

# So, We can use Segment Tree to perform both the operations(range queries and update) in O(log n) time.