# LC 283 - Move Zeroes: Move all zeroes to the end of the array

def move_zeroes(nums):
    pt = len(nums)-1

    # for i,j in enumerate(nums): #prints both the index and its corresponding elements
    #     print(i,j)
    #print(range(0, len(nums)-1))
    for i in range(0, len(nums)-1):
        #print(num)
        if nums[i] is 0: #if the element at this index is equal to 0
            nums[i], nums[pt] = nums[pt], nums[i]
            pt -= 1

    return nums

# test case: move all zeroes to the back
test = move_zeroes([0,4,0,3,7,6,0,7,0,4,5])
print(test)
# can't get last 7 to move