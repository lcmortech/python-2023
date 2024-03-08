# MERGE SORT - Sorting Algorithm (Programiz)

# emergency - hospital stay 1 (friday)
# emergency - hospital stay 2 (saturday)

# [fetched, pull]

# Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

# Using merge sort, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

# THE DIVIDE AND CONQUER TECHNIQUE

# Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.

# EXAMPLE

# Suppose we had to sort an array A. A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].

# DIVIDE
# If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r].

# CONQUER
# In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

# Combine

# When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].

# MergeSort Algorithm

# The MergeSort function repeatedly divides the array into two halves until we reach a stage where we try to perform MergeSort on a subarray of size 1 i.e. p == r.
# After that, the merge function comes into play and combines the sorted arrays into larger arrays until the whole array is merged.

MergeSort(A, p, r):
    if p > r 
        return
    q = (p+r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

# To sort an entire array, we need to call MergeSort(A, 0, length(A)-1).

# As shown in the example below, the merge sort algorithm recursively divides the array into halves until we reach the base case of array with 1 element. After that, the merge function picks up the sorted sub-arrays and merges them to gradually sort the entire array.

# The merge Step of Merge Sort

# Every recursive algorithm is dependent on a base case and the ability to combine the results from base cases. Merge sort is no different. The most important part of the merge sort algorithm is, you guessed it, merge step.

# The merge step is the solution to the simple problem of merging two sorted lists(arrays) to build one large sorted list(array).

# The algorithm maintains three pointers, one for each of the two arrays and one for maintaining the current index of the final sorted array.

# Have we reached the end of any of the arrays?
#    No:
#        Compare current elements of both #arrays 
#        Copy smaller element into sorted array
#        Move pointer of element containing #smaller element
#    Yes:
#        Copy all remaining elements of non-empty array

# Since there are no more elements remaining in the second array, and we know that both the arrays were sorted when we started, we can copy the remaining elements from the first array directly.

# Writing the Code for Merge Algorithm

# A noticeable difference between the merging step we described above and the one we use for merge sort is that we only perform the merge function on consecutive sub-arrays.

# This is why we only need the array, the first position, the last index of the first subarray(we can calculate the first index of the second subarray) and the last index of the second subarray.

# Our task is to merge two subarrays A[p..q] and A[q+1..r] to create a sorted array A[p..r]. So the inputs to the function are A, p, q and r

# The merge function works as follows:

# Create copies of the subarrays L <- A[p..q] and M <- A[q+1..r].
# Create three pointers i, j and k
#i maintains current index of L, starting at 1
# j maintains current index of M, starting at 1
# k maintains the current index of A[p..q], starting at p.
# Until we reach the end of either L or M, pick the larger among the elements from L and M and place them in the correct position at A[p..q]
# When we run out of elements in either L or M, pick up the remaining elements and put in A[p..q]
# In code, this would look like: (See programiz for example in Java)

# =========STEPS====

# Step 1: Create duplicate copies of sub-arrays to be sorted

# Step 2: Maintain current index of sub-arrays and main array

# ==========END======

# MergeSort in Python

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)