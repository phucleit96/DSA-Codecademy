# Implementation of a Stack using a Node class for a linked list

from node import Node  # Importing Node class for creating linked list nodes


class Stack:
    def __init__(self, name):
        """
        Initializes a stack with a given name.
        """
        self.size = 0
        self.top_item = None
        self.limit = 1000  # Maximum size of the stack
        self.name = name  # Name of the stack

    def push(self, value):
        """
        Adds a new item to the top of the stack.
        """
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")  # Alert when stack is full

    def pop(self):
        """
        Removes the top item from the stack and returns its value.
        """
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This stack is totally empty.")  # Alert when stack is empty

    def peek(self):
        """
        Returns the value of the top item in the stack without removing it.
        """
        if self.size > 0:
            return self.top_item.get_value()
        print("Nothing to see here!")  # Alert when stack is empty

    def has_space(self):
        """
        Checks if there is space available in the stack.
        """
        return self.limit > self.size

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return self.size == 0

    def get_size(self):
        """
        Returns the size of the stack.
        """
        return self.size

    def get_name(self):
        """
        Returns the name of the stack.
        """
        return self.name

    def print_items(self):
        """
        Prints the items in the stack.
        """
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        # Reverse the list so that the top of the stack is printed first
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))
