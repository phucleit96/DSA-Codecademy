# Define the function move_to_end that moves all occurrences of the value val to the end of the list lst
def move_to_end(lst, val):
    result = []  # Initialize an empty list to store the modified list

    # Base case: If the list is empty, return an empty list (termination condition for recursion)
    if len(lst) == 0:
        return []

    # If the first element of the list is the specified value
    if lst[0] == val:
        # Recursively call move_to_end with the sublist starting from the next element
        # This will move occurrences of val to the end of the list
        result += move_to_end(lst[1:], val)

        # Append the current element (val) to the end of the result
        result.append(lst[0])
    else:
        # If the first element is not the specified value, append it to the result
        result.append(lst[0])

        # Recursively call move_to_end with the sublist starting from the next element
        # This continues the iteration through the list
        result += move_to_end(lst[1:], val)

    return result  # Return the modified list

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))  # Call the function to move "Amber" to the end of the list

import LinkedList  # Imports a custom module named LinkedList (assumed to contain a LinkedList class)

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, value, next_node=None):
        """
        Definition for a node in a singly-linked list.

        Args:
        - value: The value to be stored in the node.
        - next_node: Reference to the next node in the list (default is None).
        """
        self.value = value
        self.next_node = next_node

# Define remove_node() to remove a node at the specified index in a singly-linked list
def remove_node(head, i):
    """
    Removes a node at the given index 'i' in a singly-linked list.

    Args:
    - head: The head node of the linked list.
    - i: The index of the node to be removed.

    Returns:
    - The head of the modified linked list after removing the node at index 'i'.
    """
    # Base cases for handling invalid inputs or empty lists
    if i < 0:  # If the index is negative, return the current head
        return head
    if head is None:  # If the list is empty, return None
        return None

    # If index 'i' is 0, remove the node by returning the next node as the new head
    if i == 0:
        return head.next_node

    # Recursively move through the list to find the node at index 'i-1'
    # Once found, update the 'next_node' reference to skip the node at index 'i'
    head.next_node = remove_node(head.next_node, i - 1)
    return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)  # Remove the node at index 1 in the linked list
print(head.flatten())  # Flatten the modified linked list and print it


# Define wrap_string() to wrap a string within angled brackets recursively 'n' times
def wrap_string(string, n):
    """
    Wraps a given string within angled brackets '<' and '>' recursively 'n' times.

    Args:
    - string: The string to be wrapped.
    - n: The number of times the string is wrapped within brackets.

    Returns:
    - The string wrapped 'n' times within angled brackets.
    """
    result = ""

    # Base case: If 'n' is less than or equal to 0, return the original string as is
    if n <= 0:
        return string

    # Recursive case: Wrap the string within '<' and '>' and concatenate the result
    result += "<"
    result += wrap_string(string, n - 1)  # Recursively wrap the string 'n-1' times
    result += ">"

    return result

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)  # Print the string "Pearl" wrapped within angled brackets three times
