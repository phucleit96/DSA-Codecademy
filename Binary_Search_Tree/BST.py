class Node:
    def __init__(self, value):
        # Initialize a node with a given value, and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty Binary Search Tree with a null root
        self.root = None

    def insert(self, value):
        # Insert a new value into the Binary Search Tree
        new_node = Node(value)

        if self.root is None:
            # If the tree is empty, set the new node as the root
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                # If the value already exists in the tree, return False (no duplicates allowed)
                return False

            if new_node.value < temp.value:
                # If the new value is less than the current node's value, go left
                if temp.left is None:
                    # If there is no left child, insert the new node as the left child
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                # If the new value is greater than the current node's value, go right
                if temp.right is None:
                    # If there is no right child, insert the new node as the right child
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # Check if the Binary Search Tree contains a specific value
        temp = self.root
        while temp is not None:
            if temp.value < value:
                # If the current node's value is less than the target value, go right
                temp = temp.right
            elif temp.value > value:
                # If the current node's value is greater than the target value, go left
                temp = temp.left
            else:
                # If the current node's value is equal to the target value, it is found
                return True
        # If the target value is not found, return False
        return False

    def __r_insert(self, current_node, value):
        # Recursive helper function to insert a value into the Binary Search Tree
        if current_node is None:
            # If the current node is None, create a new node with the given value
            return Node(value)
        if value < current_node.value:
            # If the value is less than the current node's value, recursively insert on the left
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            # If the value is greater than the current node's value, recursively insert on the right
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        # Wrapper function for the recursive insert
        if self.root is None:
            # If the tree is empty, set the root to a new node with the given value
            self.root = Node(value)
        else:
            # Otherwise, call the recursive insert function
            self.__r_insert(self.root, value)

    def min_value(self, current_node):
        # Find the minimum value in a subtree starting from the given node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        # Recursive helper function to delete a node with a given value from the Binary Search Tree
        if current_node is None:
            # If the current node is None, return None
            return None
        if value < current_node.value:
            # If the value is less than the current node's value, recursively delete on the left
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            # If the value is greater than the current node's value, recursively delete on the right
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                # Case 1: Node has no children, simply remove the node
                return None
            elif current_node.left is None:
                # Case 2: Node has one child (right), replace the node with its right child
                current_node = current_node.right
            elif current_node.right is None:
                # Case 3: Node has one child (left), replace the node with its left child
                current_node = current_node.left
            else:
                # Case 4: Node has two children, find the minimum value in the right subtree,
                # replace the node's value with the minimum, and recursively delete the minimum node
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        # Wrapper function for the recursive delete
        self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.delete_node(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""

# Create a Binary Search Tree and insert some values
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# Check if specific values are present in the tree
print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))

"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False
"""
