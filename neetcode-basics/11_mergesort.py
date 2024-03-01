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

