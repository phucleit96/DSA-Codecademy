#########################################
# COMMENTS TO EXPLAIN THE CODE'S FUNCTIONALITY
#########################################

#####
# TREENODE CLASS
#####

class TreeNode:
 """
 Represents a single node in the interactive story tree.
 Each node contains a piece of the story text and a list of choices that lead to other nodes.
 """

 def __init__(self, story_piece):
   """
   Initializes a new TreeNode object.

   Args:
     story_piece (str): The text of the story segment to be displayed at this node.
   """

   self.story_piece = story_piece
   self.choices = []  # List of child nodes that represent possible choices

 def add_child(self, node):
   """
   Adds a child node to this node, representing a possible choice.

   Args:
     node (TreeNode): The child node to be added.
   """

   self.choices.append(node)

 def traverse(self):
   """
   Starts the interactive story experience by presenting the current story segment and prompting the user for choices.
   """

   story_node = self  # Start at the current node
   print(story_node.story_piece)  # Print the initial story segment

   while len(story_node.choices) > 0:  # Continue as long as there are choices to make
     user_choice = input("Enter 1 or 2 to continue the story: ")

     if user_choice not in ["1", "2"]:
       print("Not valid choice, please choose either 1 or 2! ")

     else:
       chosen_index = int(user_choice) - 1  # Adjust for 0-based indexing
       chosen_child = story_node.choices[chosen_index]
       print(chosen_child.story_piece)  # Print the next story segment based on the user's choice
       story_node = chosen_child  # Move to the chosen child node for further choices

#####
# VARIABLES FOR TREE STRUCTURE
#####

# Create the root node and subsequent nodes for the story
story_root = TreeNode(...)  # ... represents the initial story segment (inserted here for clarity)
choice_a = TreeNode(...)
choice_b = TreeNode(...)
...  # Continue creating nodes for each story segment and choice

# Connect the nodes to form the interactive story tree
story_root.add_child(choice_a)
story_root.add_child(choice_b)
...  # Continue connecting nodes based on the story structure

#####
# TESTING AREA
#####

print("Once upon a time ...")
story_root.traverse()  # Start the interactive story experience