def move_zeroes(nums):
    pt = len(nums)-1

    for num in range(0, len(nums)-1):
        nums[num], nums[pt] = nums[pt],nums[num]
        pt -= 1

    return nums

