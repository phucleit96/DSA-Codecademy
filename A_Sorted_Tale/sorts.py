import random

# --- Bubble Sort Implementation ---
# This function implements the bubble sort algorithm, which repeatedly
# iterates through the list, comparing adjacent elements and swapping
# them if they are in the wrong order. It continues until no swaps occur,
# indicating the list is sorted.
def bubble_sort(arr, comparison_function):

 # --- Initialize variables to track swaps and sorting status ---
 swaps = 0  # Count the number of swaps made during sorting
 sorted = False  # Flag to indicate if the list is sorted

 # --- Iterate until the list is sorted ---
 while not sorted:

   # --- Assume the list is sorted initially ---
   sorted = True

   # --- Iterate through each adjacent pair of elements ---
   for idx in range(len(arr) - 1):

     # --- If the elements are in the wrong order, swap them ---
     if comparison_function(arr[idx], arr[idx + 1]):
       sorted = False  # List is not sorted yet
       arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]  # Perform the swap
       swaps += 1  # Increment the swap counter

 # --- Print the number of swaps performed ---
 print("Bubble sort: There were {0} swaps".format(swaps))

 # --- Return the sorted list ---
 return arr


# --- Quicksort Implementation ---
# This function implements the quicksort algorithm, which recursively
# divides the list into smaller sublists and sorts them individually.
# It uses a pivot element to partition the list and then calls itself
# to sort the sublists on either side of the pivot.
def quicksort(list, start, end, comparison_function):

 # --- Base case: If the list is empty or has one element, it's already sorted ---
 if start >= end:
   return

 # --- Choose a random pivot element ---
 pivot_idx = random.randrange(start, end + 1)
 pivot_element = list[pivot_idx]

 # --- Partition the list around the pivot ---
 list[end], list[pivot_idx] = list[pivot_idx], list[end]  # Move pivot to end
 less_than_pointer = start  # Pointer to track elements less than pivot

 for i in range(start, end):
   if comparison_function(pivot_element, list[i]):  # If element is less than pivot
     list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
     less_than_pointer += 1  # Move the pointer to the right

 list[end], list[less_than_pointer] = list[less_than_pointer], list[end]  # Put pivot in its final position

 # --- Recursively sort the sublists ---
 quicksort(list, start, less_than_pointer - 1, comparison_function)
 quicksort(list, less_than_pointer + 1, end, comparison_function)
