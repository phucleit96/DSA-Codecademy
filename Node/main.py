class Node:
    def __init__(self, value, link_node=None):
        # Constructor to initialize a Node object with a value and a link_node
        self.value = value  # Assigning the value to the Node
        self.link_node = link_node  # Assigning the link to another Node (default is None)

    def set_link_node(self, link_node):
        # Method to set the link_node of the current Node
        self.link_node = link_node  # Set the link_node to the provided Node

    def get_link_node(self):
        # Method to get the linked Node of the current Node
        return self.link_node  # Return the linked Node

    def get_value(self):
        # Method to get the value of the current Node
        return self.value  # Return the value of the Node


# Creating instances of Node and linking them
yacko = Node('likes to yak')  # Create a Node with the value 'likes to yak'
wacko = Node('has a penchant for hoarding snacks')  # Create a Node with the value 'has a penchant for hoarding snacks'
dot = Node('enjoys spending time in movie lots')  # Create a Node with the value 'enjoys spending time in movie lots'

# Linking the Nodes together
yacko.set_link_node(dot)  # Set dot Node as the linked Node for yacko Node
dot.set_link_node(wacko)  # Set wacko Node as the linked Node for dot Node

# Accessing linked Nodes' data
dots_data = yacko.get_link_node().get_value()  # Get the value of the Node linked to yacko
wackos_data = dot.get_link_node().get_value()  # Get the value of the Node linked to dot

# Printing the data obtained from linked Nodes
print(dots_data)  # Output: 'has a penchant for hoarding snacks'
print(wackos_data)  # Output: 'enjoys spending time in movie lots'
