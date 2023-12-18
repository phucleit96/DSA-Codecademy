# runtime: Linear - O(N)
def factorial(n):
  if n < 0:
    return ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  return n * factorial(n - 1)

factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
# ValueError "Input must be 0 or greater"

# runtime: Exponential - O(2^N)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0

def sum_digits(n):
    # base case: if input is a single digit
    if n <= 9:
        return n

    # recursive step
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

def find_min(my_list, min=None):
  if len(my_list) == 0:
    return min
  else:
    if min is None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)


def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    else:
        if my_string[0] != my_string[-1]:
            return False
        else:
            return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)

def multiplication(num1, num2):
  result = 0
  if num1 == 0 or num2 == 0:
    return result
  else:
    return num1 + multiplication(num1, num2 - 1)


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)


def depth(tree_node):
    if tree_node is None:
        return 0

    left_depth = depth(tree_node["left_child"])
    right_depth = depth(tree_node["right_child"])

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[: mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1:])

    return tree_node


# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)