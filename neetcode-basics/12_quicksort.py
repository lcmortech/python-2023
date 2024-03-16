# QUICKSORT ALGORITHM (Programiz)

# Quicksort is a sorting algorithm based on the divide and conquer approach where

# An array is divided into subarrays by selecting a pivot element (element selected from the array).

# While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
# The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
# At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

#====
# Working of Quicksort Algorithm

# 1. Select the Pivot Element
# There are different variations of quicksort where the pivot element is selected from different positions. Here, we will be selecting the rightmost element of the array as the pivot element.

# 2. Rearrange the Array
# Now the elements of the array are rearranged so that elements that are smaller than the pivot are put on the left and the elements greater than the pivot are put on the right.

## Here's how we rearrange the array:
# 1. A pointer is fixed at the pivot element. The pivot element is compared with the elements beginning from the first index.

# If the element is greater than the pivot element, a second pointer is set for that element.

# 2. If the element is greater than the pivot element, a second pointer is set for that element.

# 3. Now, pivot is compared with other elements. If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.

# 4. Again, the process is repeated to set the next greater element as the second pointer. And, swap it with another smaller element.

# 5. The process goes on until the second last element is reached.