nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))


# Function to swap elements in a list
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


# Unoptimized version of bubble sort
def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)
    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


# Optimized version of bubble sort
def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)): #range(len(arr) - 1, 0, -1):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1): #range(i)
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # Swap elements using tuple assignment (no separate swap function)
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


# Testing the unoptimized bubble sort (copying the original list to avoid modification)
bubble_sort_unoptimized(nums.copy())

# Sorting the original list using the optimized bubble sort
bubble_sort(nums)

print("POST SORT: {0}".format(nums))  # Displaying the sorted list


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

    def bubble_sort_linked_list(self):
        """
        Sorts the linked list in ascending order using the bubble sort algorithm.
        """

        # Check if the length of the linked list is less than 2
        # If so, the list is already sorted or has only one element; no sorting needed
        if self.length < 2:
            return

        sorted_list = False  # Flag to track if the list is sorted
        while not sorted_list:
            sorted_list = True  # Set to True assuming the list is sorted
            current = self.head  # Start from the head of the list

            # Traverse the list
            while current.next is not None:
                # Compare the current node's value with the value of the next node
                if current.value > current.next.value:
                    # Swap the values of the current node and its next node
                    current.value, current.next.value = current.next.value, current.value
                    sorted_list = False  # Set the flag to False as a swap occurred
                current = current.next  # Move to the next node

        # Find and set the tail of the linked list after sorting
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current


# Create a linked list and perform bubble sort on it
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort_linked_list()

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
