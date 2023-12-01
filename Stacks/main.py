from node import Node  # Import the Node class from the 'node' module

class Stack:
    def __init__(self, limit=1000):
        # Initialize the Stack class with a top_item, size, and limit
        self.top_item = None  # Represents the top item in the stack (initially empty)
        self.size = 0  # Represents the current size of the stack (number of items)
        self.limit = limit  # Represents the maximum capacity of the stack

    def push(self, value):
        # Method to add a new item (pizza) to the top of the stack
        if self.has_space():  # Check if there is space in the stack
            item = Node(value)  # Create a new Node with the provided value
            item.set_next_node(self.top_item)  # Set the new item's link to the current top_item
            self.top_item = item  # Set the new item as the new top_item
            self.size += 1  # Increment the size of the stack
            print("Adding {} to the pizza stack!".format(value))  # Print a message indicating the addition
        else:
            print("No room for {}!".format(value))  # Print a message if there's no space in the stack

    def pop(self):
        # Method to remove and deliver the top item (pizza) from the stack
        if not self.is_empty():  # Check if the stack is not empty
            item_to_remove = self.top_item  # Get the top_item to remove
            self.top_item = item_to_remove.get_next_node()  # Set the next item as the new top_item
            self.size -= 1  # Decrement the size of the stack
            print("Delivering " + item_to_remove.get_value())  # Print a message indicating delivery
            return item_to_remove.get_value()  # Return the value of the delivered item
        print("All out of pizza.")  # Print a message if the stack is empty

    def peek(self):
        # Method to peek at the top item (pizza) without removing it from the stack
        if not self.is_empty():  # Check if the stack is not empty
            return self.top_item.get_value()  # Return the value of the top_item
        print("Nothing to see here!")  # Print a message if the stack is empty

    def has_space(self):
        # Method to check if there is space available in the stack
        return self.limit > self.size  # Return True if there is space, False otherwise

    def is_empty(self):
        # Method to check if the stack is empty
        return self.size == 0  # Return True if the stack is empty, False otherwise

# Defining an empty pizza stack with a limit of 6 pizzas
pizza_stack = Stack(6)

# Adding pizzas to the stack until the limit is reached
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncommenting the line below will attempt to add another pizza beyond the limit
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncommenting the line below will attempt to deliver a pizza when the stack is empty
pizza_stack.pop()
