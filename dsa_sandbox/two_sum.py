#NOTES

#Brute Force
def two_sum(list, t):

    new_list = []
    for i in range(len(list)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == t:
                return [i, j]
            
    return new_list
