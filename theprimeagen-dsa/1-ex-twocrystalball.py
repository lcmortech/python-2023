##NOTES

# Given two crystal balls that will break if dropped from high enough distance, determine the exact spot in which it will break in the most optimized way. 
# This is a question about arrays
# The runtime is the square route of N, or sqrt(N)
import math

def two_ball(breaks_bool, target):
    jump_amount = math.floor(math.sqrt(len(breaks_bool)))
    i = jump_amount

    for i in range(0,jump_amount):
        if breaks_bool[i]:
            break
    
    i -= jump_amount

    for j in range(len(jump_amount)+1):
        if breaks_bool[i]:
            return i
    
    return -1