#NOTES

#Brute Force O(n^2)
# def two_sum(nums, t):

#     new_nums = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == t:
#                 return [i, j]
            
#     return new_nums


#Hashmap O(n)
def two_sum(nums, t):
    new_map = {}
    count = len(nums)

    for i in range(count):
        diff = t - nums[i]
        if diff in new_map:
            return [new_map[diff], i]
        
    return []

#TEST 

test = two_sum([3,6,4,5,], 6)
test2 = two_sum([3,6,4,5,], 10)
print(test)
print(test2)
