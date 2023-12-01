class Node:
    def __init__(self, value, next_node=None):
        """
        Initialize a Node with a value and a reference to the next node.

        Args:
        - value: The value to be stored in the node.
        - next_node: Reference to the next node.
        """
        self.value = value  # Value of the node
        self.next_node = next_node  # Reference to the next node

    # Getters and setters for next_node and value


class LinkedList:
    def __init__(self, value=None):
        """
        Initialize a Linked List with a head node.

        Args:
        - value: The initial value for the head node.
        """
        self.head_node = Node(value)  # Head node of the linked list

    def get_head_node(self):
        """
        Get the head node of the linked list.
        """
        return self.head_node

    def insert_beginning(self, new_value):
        """
        Insert a new node at the beginning of the linked list.

        Args:
        - new_value: The value for the new node to be inserted.
        """
        new_node = Node(new_value)  # Create a new node with the provided value
        new_node.set_next_node(self.head_node)  # Set the next node of the new node to the current head
        self.head_node = new_node  # Update the head node to the new node

    def stringify_list(self):
        """
        Create a string representation of the linked list.
        Returns a string containing node values separated by newlines.
        """
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        """
        Remove a node with a specific value from the linked list.

        Args:
        - value_to_remove: The value of the node to be removed.
        """
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            # If the value to remove is in the head node, update head node to the next node
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    # If the next node's value matches the value to remove, update the link to skip the node
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node  # Move to the next node in the linked list
