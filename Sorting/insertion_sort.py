def insertion_sort(my_list):
    """
    Sorts a list in ascending order using the insertion sort algorithm.

    Args:
    - my_list (list): The input list to be sorted.

    Returns:
    - list: The sorted list in ascending order.
    """
    for i in range(1, len(my_list)):  # Iterate through the list starting from the second element
        temp = my_list[i]  # Store the current element to be placed in its correct position
        j = i - 1  # Initialize a pointer to the element before the current one

        # Move elements of the sorted segment that are greater than 'temp' to one position ahead
        while j >= 0 and temp < my_list[j]:
            my_list[j+1] = my_list[j]  # Shift the larger element one position ahead
            my_list[j] = temp  # Place 'temp' in the position vacated by the larger element
            j -= 1  # Move the pointer to the previous element

    return my_list  # Return the sorted list


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

    def insertion_sort_ll(self):
        """
        Sorts the linked list in ascending order using the insertion sort algorithm.
        """
        if self.length < 2:
            return

        sorted_list_head = self.head  # Initialize the sorted list with the head of the linked list
        unsorted_list_head = self.head.next  # Initialize the unsorted list starting from the second node

        sorted_list_head.next = None  # Mark the end of the sorted list

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next  # Move to the next node in the unsorted list

            if current.value < sorted_list_head.value:
                # Insert the current node at the beginning of the sorted list
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                # Search for the correct position to insert the current node in the sorted list
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current

        self.head = sorted_list_head  # Update the head of the linked list to the sorted list head

        # Find and update the tail of the linked list after sorting
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp


# Create a linked list and perform insertion sort on it
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort_ll()

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