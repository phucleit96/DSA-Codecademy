def factorial(n):
  if n < 0:
    return ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  factor = 1
  for i in range(2, n+1):
    factor *= i
  return factor


# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

def fibonacci(n):
  fibs = [0, 1]
  if n <= len(fibs) - 1:
    return fibs[n]
  else:
    while n > len(fibs) - 1:
      next_fib = fibs[-1] + fibs[-2]
      fibs.append(next_fib)
  return fibs[n]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)

# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

sum_digits(12)
# 1 + 2
# 3
sum_digits(552)
# 5 + 5 + 2
# 12
sum_digits(123456789)
# 1 + 2 + 3 + 4...
# 45

def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

find_min([42, 17, 2, -1, 67])
# -1
find_min([])
# None
find_min([13, 72, 19, 5, 86])
# 5


def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True

is_palindrome("abba")
# True
is_palindrome("abcba")
# True
is_palindrome("")
# True
is_palindrome("abcd")
# False

def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

multiplication(3, 7)
# 21
multiplication(5, 5)
# 25
multiplication(0, 4)
# 0

def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result

two_level_tree = {
"data": 6,
"left_child":
  {"data": 2}
}

four_level_tree = {
"data": 54,
"right_child":
  {"data": 93,
   "left_child":
     {"data": 63,
      "left_child":
        {"data": 59}
      }
   }
}


depth(two_level_tree)
# 2
depth(four_level_tree)
# 4

