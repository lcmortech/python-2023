def smallest_val(arr):

    if not arr or arr[0] == None:
        return arr
    else:    
        min_val = arr[0]
        nums = len(arr)
        for i in range(nums):
            if min_val > i:
                min_val = i
        return min_val

    print(smallest_val([2,7,4,5,8]))
    


