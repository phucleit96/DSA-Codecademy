# Import necessary classes and functions from TreeNode module
from TreeNode import TreeNode, sample_root_node, print_path, print_tree

# Print the tree structure
print_tree(sample_root_node)

# Define a Depth-First Search (DFS) function to find a path from the root to a target value
def dfs(root, target, path=()):
    # Append the current node to the path
    path = path + (root,)

    # Check if the current node's value matches the target value
    if root.value == target:
        return path

    # Recursively search for the target value in the children of the current node
    for child in root.children:
        path_found = dfs(child, target, path)

        # If a path is found in the child, return the path
        if path_found is not None:
            return path_found

    # If the target value is not found in the subtree, return None
    return None

# Use the DFS function to find a path to the target value "F" in the sample root node
path = dfs(sample_root_node, "F")

# Print the resulting path
print(path)

# Expected tree structure:
# A
# ├─B
#    ├─D
#    └─E
# └─C
#    ├─F
#    └─G

# Expected output:
# (A, C, F)
