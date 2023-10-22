## NOTES
# A very good practice to get into is being able to visualize the problem, discuss it with boxes and arrows, and program it. Its definitely a core competency that will follow you for life.

# What's the way something fails? If we search the entire length of the array and the item is not there
# As your input grows so does the time it takes linearly



def linear_search(haystack, targ):
    for needle in haystack:
        if needle == targ:
            return True
        
    return False
        

