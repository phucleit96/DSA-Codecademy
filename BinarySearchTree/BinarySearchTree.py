import random


class BinarySearchTree:
    def __init__(self, value, depth=1):
        # Initialize a node with a given value and depth
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert a new value into the tree
        if (value < self.value):
            # If the value is less than the current node's value, go to the left
            if (self.left is None):
                # If there is no left child, create a new node and assign it to the left child
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                # If there is a left child, recursively insert into the left subtree
                self.left.insert(value)
        else:
            # If the value is greater than or equal to the current node's value, go to the right
            if (self.right is None):
                # If there is no right child, create a new node and assign it to the right child
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                # If there is a right child, recursively insert into the right subtree
                self.right.insert(value)

    def get_node_by_value(self, value):
        # Search for a node with a specific value in the tree
        if (self.value == value):
            # If the current node's value matches the target value, return the current node
            return self
        elif ((self.left is not None) and (value < self.value)):
            # If there is a left child and the target value is less than the current node's value,
            # recursively search in the left subtree
            return self.left.get_node_by_value(value)
        elif ((self.right is not None) and (value >= self.value)):
            # If there is a right child and the target value is greater than or equal to
            # the current node's value, recursively search in the right subtree
            return self.right.get_node_by_value(value)
        else:
            # If no match is found, return None
            return None

    def depth_first_traversal(self):
        # Perform a depth-first traversal (inorder) of the tree
        if (self.left is not None):
            # Traverse the left subtree recursively
            self.left.depth_first_traversal()
        # Print the current node's depth and value
        print(f'Depth={self.depth}, Value={self.value}')
        if (self.right is not None):
            # Traverse the right subtree recursively
            self.right.depth_first_traversal()


# Main program
print("Creating Binary Search Tree rooted at value 15:")
# Create a Binary Search Tree with the root value of 15
tree = BinarySearchTree(15)

# Insert 10 random values into the tree
for x in range(10):
    tree.insert(random.randint(0, 100))

print("Printing the inorder depth-first traversal:")
# Print the inorder depth-first traversal of the tree
tree.depth_first_traversal()

# Creating Binary Search Tree rooted at value 15:
# Tree node 69 added to the right of 15 at depth 2
# Tree node 33 added to the left of 69 at depth 3
# Tree node 39 added to the right of 33 at depth 4
# Tree node 72 added to the right of 69 at depth 3
# Tree node 19 added to the left of 33 at depth 4
# Tree node 12 added to the left of 15 at depth 2
# Tree node 84 added to the right of 72 at depth 4
# Tree node 88 added to the right of 84 at depth 5
# Tree node 82 added to the left of 84 at depth 5
# Tree node 81 added to the left of 82 at depth 6
# Printing the inorder depth-first traversal:
# Depth=2, Value=12
# Depth=1, Value=15
# Depth=4, Value=19
# Depth=3, Value=33
# Depth=4, Value=39
# Depth=2, Value=69
# Depth=3, Value=72
# Depth=6, Value=81
# Depth=5, Value=82
# Depth=4, Value=84
# Depth=5, Value=88