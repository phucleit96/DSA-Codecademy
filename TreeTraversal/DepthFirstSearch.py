# Define a Node class for the binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a new value into the binary search tree
    def insert(self, value):
        new_node = Node(value)
        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return True
        # Traverse the tree to find the correct position for the new node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Value already exists, return False
            if new_node.value < temp.value:
                # If the new value is less than the current node, move to the left
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                # If the new value is greater than or equal to the current node, move to the right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Method to check if a value is present in the binary search tree
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        # Traverse the tree to find the value
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True  # Value found, return True
        return False  # Value not found, return False

    # Method to perform Breadth-First Search (BFS) on the binary search tree
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            # Enqueue the left and right children if they exist
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    # Method to perform Depth-First Search (DFS) in pre-order on the binary search tree
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            # Recursively traverse the left subtree
            if current_node.left is not None:
                traverse(current_node.left)
            # Recursively traverse the right subtree
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    # Method to perform Depth-First Search (DFS) in post-order on the binary search tree
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            # Recursively traverse the left subtree
            if current_node.left is not None:
                traverse(current_node.left)
            # Recursively traverse the right subtree
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    # Method to perform Depth-First Search (DFS) in in-order on the binary search tree
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            # Recursively traverse the left subtree
            if current_node.left is not None:
                traverse(current_node.left)
            # Append the value of the current node
            results.append(current_node.value)
            # Recursively traverse the right subtree
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

# Create a binary search tree and insert values
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# Print the result of DFS in-order traversal
print(my_tree.dfs_in_order())

"""
    EXPECTED OUTPUT:
    ----------------
    [18, 21, 27, 47, 52, 76, 82]
"""
