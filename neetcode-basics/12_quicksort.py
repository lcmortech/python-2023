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

# 6. Finally, the pivot element is swapped with the second pointer.

#

# 3. Divide Subarrays
# Pivot elements are again chosen for the left and the right sub-parts separately. And, step 2 is repeated.

# The subarrays are divided until each subarray is formed of a single element. At this point, the array is already sorted.

# ==== CODE EXAMPLE ====
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

# Quicksort Complexity

#Time Complexity	 
#Best	O(n*log n)
#Worst	O(n2)
#Average	O(n*log n)
#Space Complexity	O(log n)
#Stability	No

# 1. Time Complexities

#Worst Case Complexity [Big-O]: O(n2)
#It occurs when the pivot element picked is either the greatest or the smallest element.

#This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only on this sub-array.

#However, the quicksort algorithm has better performance for scattered pivots.
#Best Case Complexity [Big-omega]: O(n*log n)
#It occurs when the pivot element is always the middle element or near to the middle element.
#Average Case Complexity [Big-theta]: O(n*log n)
#It occurs when the above conditions do not occur.

# 2. Space Complexity
#The space complexity for quicksort is O(log n).