## NOTES

# Yes, let's do bubble sort. Usually the first algorithm in almost every major source is insertion sort, but I find it so boring. Let's do bubble sort!
# As my teacher once said...to the whiteboard!
# Any x sub-i/ith poisiton in the array is going to be less than or equal to any i+1
# starts in 0-eth position (first position) its gonna go to the end of the array. It goes to the +1 next to it and asks, if I'm larger than you, let's swap positions.
# A singular iteration will always produce the largest item in the last spot/position. We can go up to, but not include the last position
# An array with one element is ALWAYS sorted

#O(n^2)
def bubsort(list):
    n_length = len(list)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):

            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]

        if not swapped:
            return
        
# Auxiliary Space O(1)
def bubsortopt(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return
