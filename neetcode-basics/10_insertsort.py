# Algorith - INSERT SORT (Programiz)

# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

# Insertion sort works similarly as we sort cards in our hand in a card game.

# We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place.

# A similar approach is used by insertion sort.

# Pseudo Code Example
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort