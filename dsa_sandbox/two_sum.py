#NOTES

#Brute Force
def two_sum(nums, t):

    new_nums = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == t:
                return [i, j]
            
    return new_nums

#TEST

test = two_sum([3,6,4,5,], 6)
test2 = two_sum([3,6,4,5,], 10)
print(test)
print(test2)
