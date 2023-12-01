from node import Node  # Importing the Node class

class Queue:
    def __init__(self, max_size=None):
        # Initialize the Queue with head, tail, max_size, and size attributes
        self.head = None  # Representing the front of the queue
        self.tail = None  # Representing the rear of the queue
        self.max_size = max_size  # Maximum capacity of the queue (if specified)
        self.size = 0  # Current size of the queue

    def enqueue(self, value):
        # Method to add an item to the rear of the queue (enqueue operation)
        if self.has_space():  # Check if there is space in the queue
            item_to_add = Node(value)  # Create a new Node with the provided value
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")  # Print the added item
            if self.is_empty():  # If the queue is empty
                self.head = item_to_add  # Set both head and tail to the new item
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)  # Set the new item as the next node for the tail
                self.tail = item_to_add  # Update the tail to the new item
            self.size += 1  # Increment the size of the queue
        else:
            print("Sorry, no more room!")  # Print a message if there's no space

    def dequeue(self):
        # Method to remove and retrieve an item from the front of the queue (dequeue operation)
        if self.get_size() > 0:  # Check if the queue is not empty
            item_to_remove = self.head  # Get the item to remove (head of the queue)
            print(str(item_to_remove.get_value()) + " is served!")  # Print the served item
            if self.get_size() == 1:  # If only one item is present in the queue
                self.head = None  # Set both head and tail to None
                self.tail = None
            else:
                self.head = self.head.get_next_node()  # Update the head to the next item in the queue
            self.size -= 1  # Decrement the size of the queue
            return item_to_remove.get_value()  # Return the value of the served item
        else:
            print("The queue is totally empty!")  # Print a message if the queue is empty

    def peek(self):
        # Method to peek at the item at the front of the queue without removing it
        if self.size > 0:  # Check if the queue is not empty
            return self.head.get_value()  # Return the value of the item at the head
        else:
            print("No orders waiting!")  # Print a message if the queue is empty

    def get_size(self):
        # Method to get the current size of the queue
        return self.size  # Return the size of the queue

    def has_space(self):
        # Method to check if there is space available in the queue (based on max_size)
        if self.max_size is None:  # If max_size is not specified (unbounded queue)
            return True
        else:
            return self.max_size > self.get_size()  # Return True if there is space, False otherwise

    def is_empty(self):
        # Method to check if the queue is empty
        return self.size == 0  # Return True if the queue is empty, False otherwise

# Creating a deli line with a maximum capacity of 10 orders
deli_line = Queue(10)

# Adding orders to the deli line
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ... (other orders added)

# Uncommenting the line below will attempt to add another order when the queue is at its maximum capacity
deli_line.enqueue("western omelet with home fries")

# Delivering orders from the front of the queue
print("The first order will be " + deli_line.peek())
deli_line.dequeue()
# ... (other orders served)

# Uncommenting the line below will attempt to serve an order when the queue is empty
deli_line.dequeue()
