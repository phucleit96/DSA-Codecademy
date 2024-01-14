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