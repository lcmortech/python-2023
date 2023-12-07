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
    new_map = {} #create a dictionary instead of a list
    count = len(nums) #intiate a counter using the length of the inputted list

    for i in range(count): # for each index in the length of nums
        diff = t - nums[i] # variable that is the difference between the target number(vsl) from two items(val)
        if diff in new_map: # if the diff of the target number is in the dictionary
            return [new_map[diff], i] # return the sum if found (val found added to the diff that makes the target(sum))
        
    return []

#TEST 

test = two_sum([3,6,4,5,], 6)
test2 = two_sum([3,6,4,5,], 10)
print(test)
print(test2)
