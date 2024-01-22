class MaxHeap:
  def __init__(self):
    # Initialize an empty heap list with a None at the 0th index and set the count to 0
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    # Given an index, calculate the index of its parent
    return idx // 2

  def left_child_idx(self, idx):
    # Given an index, calculate the index of its left child
    return idx * 2

  def right_child_idx(self, idx):
    # Given an index, calculate the index of its right child
    return idx * 2 + 1

  def child_present(self, idx):
    # Check if a node has a left child (assumes complete binary tree)
    return self.left_child_idx(idx) <= self.count
  # END OF HEAP HELPER METHODS

  def add(self, element):
    # Add a new element to the heap, increment count, and restore the max heap property
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()

  def heapify_up(self):
    # Restore the max heap property by moving the last added element up the heap
    print("Heapifying up")
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print("Swapping {0} with {1}".format(parent, child))
        # Swap parent and child if the parent is smaller than the child
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))

  def retrieve_max(self):
    # Retrieve and remove the maximum element, then restore the max heap property
    if self.count == 0:
      print("No items in heap")
      return None
    max_value = self.heap_list[1]
    print("Removing: {0} from {1}".format(max_value, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))
    self.heapify_down()
    return max_value

  def heapify_down(self):
    # Restore the max heap property by moving the first element down the heap
    idx = 1
    while self.child_present(idx):
      print("Heapifying down!")
      larger_child_idx = self.get_larger_child_idx(idx)
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      if parent < child:
        # Swap parent and larger child if the parent is smaller than the child
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      idx = larger_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")

  def get_larger_child_idx(self, idx):
    # Determine the index of the larger child (either left or right)
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child > right_child:
        print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
        return self.left_child_idx(idx)
      else:
        print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
        return self.right_child_idx(idx)


from max_heap import MaxHeap


def heapsort(lst):
  # Initialize an empty list to store the sorted elements
  sort = []

  # Create an instance of MaxHeap
  max_heap = MaxHeap()

  # Add each element from the input list to the max heap
  for idx in lst:
    max_heap.add(idx)

  # Retrieve the maximum element from the max heap and insert it at the beginning of the sorted list
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)

  return sort


# Example usage
my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)

# Adding: 99 to [None]
# Heapifying up
# Heap Restored [None, 99]
# Adding: 22 to [None, 99]
# Heapifying up
# Heap Restored [None, 99, 22]
# Adding: 61 to [None, 99, 22]
# Heapifying up
# Heap Restored [None, 99, 22, 61]
# Adding: 10 to [None, 99, 22, 61]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10]
# Adding: 21 to [None, 99, 22, 61, 10]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21]
# Adding: 13 to [None, 99, 22, 61, 10, 21]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21, 13]
# Adding: 23 to [None, 99, 22, 61, 10, 21, 13]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21, 13, 23]
# Removing: 99 from [None, 99, 22, 61, 10, 21, 13, 23]
# Last element moved to first: [None, 23, 22, 61, 10, 21, 13]
# Heapifying down!
# Right child 61 is larger than left child 22
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 61, 22, 23, 10, 21, 13]
#
# Removing: 61 from [None, 61, 22, 23, 10, 21, 13]
# Last element moved to first: [None, 13, 22, 23, 10, 21]
# Heapifying down!
# Right child 23 is larger than left child 22
# HEAP RESTORED! [None, 23, 22, 13, 10, 21]
#
# Removing: 23 from [None, 23, 22, 13, 10, 21]
# Last element moved to first: [None, 21, 22, 13, 10]
# Heapifying down!
# Left child 22 is larger than right child 13
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 22, 21, 13, 10]
#
# Removing: 22 from [None, 22, 21, 13, 10]
# Last element moved to first: [None, 10, 21, 13]
# Heapifying down!
# Left child 21 is larger than right child 13
# HEAP RESTORED! [None, 21, 10, 13]
#
# Removing: 21 from [None, 21, 10, 13]
# Last element moved to first: [None, 13, 10]
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 13, 10]
#
# Removing: 13 from [None, 13, 10]
# Last element moved to first: [None, 10]
# HEAP RESTORED! [None, 10]
#
# Removing: 10 from [None, 10]
# Last element moved to first: [None]
# HEAP RESTORED! [None]
#
# [10, 13, 21, 22, 23, 61, 99]