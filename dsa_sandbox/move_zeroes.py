def move_zeroes(nums):
    pt = len(nums)-1

    for i,j in enumerate(nums):
        print(i,j)

    for num in range(0, len(nums)-1):
        print(num)
        if nums[num] == 0: #if the element at this index is equal to 0
            nums[num], nums[pt] = nums[pt], nums[num]
            pt -= 1

    return nums

# test case
test = move_zeroes([0,4,0,3,0,6,0,7,0,4,0])
print(test)