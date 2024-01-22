def merge_sort(items):
  """Sorts a list of items using the merge sort algorithm."""

  if len(items) <= 1:
    """Base case: A list of zero or one element is already sorted."""
    return items

  middle_index = len(items) // 2
  """Divide the list into two halves."""
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  """Recursively sort the left and right halves."""
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  """Merge the sorted halves back together."""
  return merge(left_sorted, right_sorted)

def merge(left, right):
  """Merges two sorted lists into a single sorted list."""

  result = []  # Create an empty list to hold the merged results

  while (left and right):
    """Compare the first elements of each list and append the smaller one to the result."""
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)  # Remove the appended element from the left list
    else:
      result.append(right[0])
      right.pop(0)  # Remove the appended element from the right list

  """Append any remaining elements from either list."""
  result += left
  result += right

  return result

# Test cases
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, ...]  # List shortened for brevity
unordered_list3 = [860, 380, 151, 585, 743, 542, ...]  # List shortened for brevity

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)
print(ordered_list1)
print(ordered_list2)
print(ordered_list3)



class Node:
  """Represents a single node in a linked list."""

  def __init__(self, value):
    """Initializes a node with a value."""
    self.value = value
    self.next = None  # Points to the next node in the list


class LinkedList:
  """Represents a linked list of nodes."""

  def __init__(self, value):
    """Initializes the linked list with a head node."""
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node  # Keeps track of the last node in the list
    self.length = 1

  def print_list(self):
    """Prints the values of all nodes in the linked list."""
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    """Adds a new node with the given value to the end of the list."""
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node  # Link the new node to the current tail
      self.tail = new_node  # Update the tail pointer
      self.length += 1


def merge(self, other_list):
  """Merges this linked list with another linked list in sorted order."""

  # Get the head nodes of both lists
  other_head = other_list.head

  # Create a dummy node to simplify handling the merged list's head
  dummy = Node(0)  # Value doesn't matter, as it won't be part of the final list
  current = dummy  # Start building the merged list from the dummy node

  # Iterate through both lists simultaneously, comparing values and appending nodes
  while self.head is not None and other_head is not None:
    if self.head.value < other_head.value:
      current.next = self.head
      self.head = self.head.next
    else:
      current.next = other_head
      other_head = other_head.next
    current = current.next  # Move to the next position in the merged list

  # Append any remaining nodes from either list
  current.next = self.head if self.head is not None else other_head

  # Update the tail of the merged list
  self.tail = other_list.tail if current.next is other_head else self.tail

  # Set the head of the merged list to the node after the dummy node
  self.head = dummy.next

  # Update the length of the merged list
  self.length += other_list.length

