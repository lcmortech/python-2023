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

