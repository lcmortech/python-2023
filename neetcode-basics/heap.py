 # Heap Data Structure (Programiz)

 # Max-Heap Data Structure

 def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 1

    if l > n and arr[i] < arr[l]:
        largest = l