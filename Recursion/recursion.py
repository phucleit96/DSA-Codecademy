# This function calculates the sum of all numbers from a given positive number 'n' down to 1.
# It uses a technique called recursion, where the function calls itself with a smaller number each time until it reaches 1.
# For example, if n = 7, it adds 7 + 6 + 5 + 4 + 3 + 2 + 1 and returns the total sum.
def sum_to_one(n):
  if n == 1:  # If the number reaches 1, stop recursion and return 1
    return n
  print("Recursing with input: {0}".format(n))  # This line displays the current number in the recursive process
  return n + sum_to_one(n-1)  # It adds the current number to the result of the function called with n-1

# Test the sum_to_one function with the number 7 and print the result
print(sum_to_one(7))

# This function calculates the factorial of a number 'n'. For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
# It uses recursion by breaking down the problem into smaller parts: n! = n * (n-1)!
def factorial(n):
  if n == 0 or n == 1:  # Factorial of 0 and 1 is 1, so return n if n is 0 or 1
    return n
  return factorial(n-1) * n  # Recursively multiplies n with the factorial of n-1

# Test the factorial function with inputs 12 and a very large number 10001020102012012 and print the results
print(factorial(12))
print(factorial(10001020102012012))

# This function generates all possible subsets (the power set) of a given list.
# For example, if the input list is ['a', 'b', 'c'], it will return [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
# It uses recursion by taking one element at a time and generates subsets with and without that element.
def power_set(my_list):
    if len(my_list) == 0:  # If the list is empty, return a list with an empty list as the only subset
        return [[]]
    power_set_without_first = power_set(my_list[1:])  # Generate subsets without the first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]  # Generate subsets with the first element
    return with_first + power_set_without_first  # Combine both subsets

# Create a power set of a list of universities and print each subset
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)
for set in power_set_of_universities:
    print(set)

# This function 'flattens' a nested list, meaning it converts a list with inner lists into a single flat list.
# For example, [['a', 'b'], 'c', ['d', ['e', 'f']]] becomes ['a', 'b', 'c', 'd', 'e', 'f'].
# It uses recursion to process each element in the list, checking if it's a list itself or an individual element.
def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):  # If the element is a list, recursively call flatten to handle nested lists
      print("List found!")
      flat_list = flatten(i)
      result += flat_list
    else:  # If the element is not a list, add it to the result list
      result.append(i)
  return result

# Test the flatten function with a list of planets containing nested lists and print the flattened list
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

# This function calculates the nth number in the Fibonacci sequence using recursion.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# For example, Fibonacci(5) = 0 + 1 + 1 + 2 + 3 = 5.
def fibonacci(n):
  if n == 1 or n == 0:  # The sequence starts from 0 and 1, so return n if n is 0 or 1
    return n
  return fibonacci(n-1) + fibonacci(n-2)  # Recursively calculates Fibonacci numbers

# Calculate the 5th number in the Fibonacci sequence and print the result
fibonacci(5)

# This function builds a binary search tree (BST) from a sorted list of numbers.
# It recursively constructs the tree by finding the middle element as the root and building subtrees for left and right elements.
def build_bst(my_list):
  if len(my_list) == 0:  # If the list is empty, return "No Child"
    return "No Child"
  middle_idx = len(my_list) // 2  # Find the index of the middle element
  middle_value = my_list[middle_idx]  # Get the middle element as the root of the tree
  print(f"Middle index: {middle_idx}")
  print(f"Middle value: {middle_value}")
  tree_node = {"data": middle_value}  # Create a tree node with the middle value as data
  tree_node["left_child"] = build_bst(my_list[:middle_idx])  # Recursively build the left subtree
  tree_node["right_child"] = build_bst(my_list[middle_idx+1:])  # Recursively build the right subtree
  return tree_node

# Build a binary search tree from a sorted list and print the tree structure
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
