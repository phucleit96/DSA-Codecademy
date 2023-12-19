def selection_sort(my_list):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
    - my_list (list): The input list to be sorted.

    Returns:
    - list: The sorted list in ascending order.
    """

    for i in range(len(my_list) - 1):
        min_index = i  # Assume the current index has the minimum value initially
        for j in range(i + 1, len(my_list)):
            # Find the index of the minimum element in the unsorted part of the list
            if my_list[j] < my_list[min_index]:
                min_index = j

        # Swap the current element with the minimum element if they are not the same
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list


# Test the selection_sort function
print(selection_sort([4, 2, 6, 5, 1, 3]))

# Expected output:
# [1, 2, 3, 4, 5, 6]

class Node:
    def __init__(self, value):
        """
        Initializes a Node object with a given value.

        Args:
        - value: Value to be stored in the Node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        Initializes a LinkedList object with a Node containing the given value as its head.

        Args:
        - value: Value to be set as the initial value of the LinkedList.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints all values present in the linked list.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds a new Node with the given value at the end of the linked list.

        Args:
        - value: Value to be added to the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def selection_sort_ll(self):
        """
        Sorts the linked list in ascending order using the selection sort algorithm.
        """
        if self.length < 2:
            return

        current = self.head
        while current.next is not None:
            # Assume the current node has the minimum value initially
            min_node = current
            temp = current.next

            # Find the node with the minimum value in the remaining unsorted part of the list
            while temp is not None:
                if temp.value < min_node.value:
                    min_node = temp
                temp = temp.next

            # Swap values between the current node and the node with the minimum value
            if current != min_node:
                current.value, min_node.value = min_node.value, current.value

            current = current.next  # Move to the next node


# Create a linked list and perform selection sort on it
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort_ll()

print("\nSorted Linked List:")
my_linked_list.print_list()

# Expected output:
# Linked List Before Sort:
# 4
# 2
# 6
# 5
# 1
# 3
# Sorted Linked List:
# 1
# 2
# 3
# 4
# 5
# 6
