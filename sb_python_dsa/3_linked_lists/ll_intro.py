# Our First Data Structure!
# Does not have indexes
# All of the nodes are all over the place, not contiguous like in a normal list
# We have a variable called head that points to the first item/node in the list
# Then we have a variable called tail that points to the last node in the list
# The other nodes point to next until the last node which points to none
# Each node is spread out in different places in memory, but because each points to the next, we can find all our nodes without losing data
# This is opposed to a list that has contigous items that are accessed through the indexes as O(1), because we can map all of these indexes to a specific address in memory
