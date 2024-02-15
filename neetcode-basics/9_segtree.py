# SEGMENT TREE DATA STRUCTURE (Geek4Geeks)

# A Segment Tree is a data structure that allows programmers to solve range queries over the given array effectively and to modifying the array values. Basically, Segment Tree is a very flexible and efficient data structure and a large number of problems can be solved with the help of segment trees.

# Representation of Segment trees 
# Leaf Nodes are the elements of the input array. 
# Each internal node represents some merging of the leaf nodes. The merging may be different for different problems. For this problem, merging is sum of leaf nodes under a node.
# An array representation of tree is used to represent Segment Trees. 

# For each node at index i, the left child is at index (2*i+1), right child at (2*i+2) and the parent is at  (⌊(i – 1) / 2⌋).
