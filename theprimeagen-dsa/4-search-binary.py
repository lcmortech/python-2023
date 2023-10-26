## NOTES

# This second algorithm is a bit pof a doosy, but its definitely a basis for other algorithms we will encounter.
# An important question you should always ask for your dataset: Is it ordered? If it is, there are new advantages you can take with that data
# Lets say it this time. So how can we search this array?
# First, let's come up with the algorithm together
# The worst case scenario is when the value's not in the array and you will halve it over and over again until the end.
# Condition 1: If value if needle we return it
# Condtition 2: The value is larger than the midpoint
# Condition 3: The value is lower than the midpoint. Adjust the midpoint plus 1
# The high needs to equal the midpoint
# Low is always inclusive and Hi is always exclusive
# Exit Condition: Lord's loop: The Do While Loop: Lo < Hi, then return False
# If you're returning the index, you're returning -1, or a sentinal value
# You don't want to use less than or equal because then your pointers will cross the line and be behind each other
# This is all under the assumption that the array is sorted. It CANNOT be done on na unsorted array/data structure
import math

def binarysearch(arr, targ):
    lo = 0
    hi = len(arr)-1 #add -1 because it's zero index. full length of the list as a hi point (int)
    mid = math.floor(lo + (hi - lo)/2) # don't forget to divide by 2!
    val = arr[mid]

    while lo < hi:
        if val == targ:
            return True
        elif val > targ:
            hi = mid
        elif val < targ:
            lo = mid + 1 # drop the midpoint. you don't want to see it again
    return False

find_targ = binarysearch([5,2,6,7,8],6)
print(find_targ)
find_targ = binarysearch([5,2,6,7,8],11)
print(find_targ)
   