# # LC 283 - Move Zeroes: Move all zeroes to the end of the array

# def move_zeroes(nums):
#     pt = len(nums)-1

#     # for i,j in enumerate(nums): #prints both the index and its corresponding elements
#     #     print(i,j)
#     #print(range(0, len(nums)-1))
#     for i in range(0, pt):
#         print(i)
#         if nums[i] == 0 and nums[pt] > 0: #if the element at this index is equal to 0
#             nums[i], nums[pt] = nums[pt], nums[i] #swap with element at the last index of the array
#             pt -= 1
#         elif nums[i] == 0 and nums[pt] == 0:
#             pass

#     return nums

# # test case
# test = move_zeroes([0,4,0,3,7,6,0,7,0,4,5])
# print(test)
# # one zero switches with a zero at the end (edge case), leaving a zero behind
# # possibly fix with recursion?

def move_zeroes(arr):
    pt = len(arr)-1

    for i in range(0, pt):
        
        if arr[pt] == 0:
            pass
        elif arr[i] == 0:
            arr[i], arr[pt] = arr[pt], arr[i]
            pt -= 1
    return arr


# test case
test = move_zeroes([0,4,0,3,7,6,0,7,0,4,5])
print(test)
# one zero switches with a zero at the end (edge case), leaving a zero behind
# possibly fix with recursion?