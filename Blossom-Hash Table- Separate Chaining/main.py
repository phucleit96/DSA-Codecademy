from linked_list import Node, LinkedList  # Importing necessary classes for linked list operations
from blossom_lib import flower_definitions  # Importing flower definitions from an external library

class HashMap:
    def __init__(self, size):
        # Initialization of HashMap with a given size
        self.array_size = size
        # Creating an array to hold linked lists
        self.array = [LinkedList() for _ in range(self.array_size)]

    # Function to hash the given key
    def hash(self, key):
        # Encoding the key into bytes
        key_bytes = key.encode()
        # Calculating a hash code by summing up the bytes of the key
        hash_code = sum(key_bytes)
        return hash_code

    # Function to compress the hash code within the array size
    def compressor(self, hash_code):
        return hash_code % self.array_size

    # Function to assign a key-value pair to the HashMap
    def assign(self, key, value):
        # Getting the index where the key-value pair will be placed in the array
        array_index = self.compressor(self.hash(key))
        # Creating a payload (Node) to hold the key-value pair
        payload = Node([key, value])
        # Getting the linked list at the calculated index
        list_at_array = self.array[array_index]
        # Iterating through the linked list
        for item in list_at_array:
            # Checking if the key already exists in the list
            if item[0] == key:
                # If key exists, update the value
                item[1] = value
                return
        # If key does not exist, insert the payload into the linked list
        list_at_array.insert(payload)

    # Function to retrieve the value for a given key
    def retrieve(self, key):
        # Getting the index where the key-value pair is located in the array
        array_index = self.compressor(self.hash(key))
        # Getting the linked list at the calculated index
        list_at_index = self.array[array_index]
        # Iterating through the linked list
        for item in list_at_index:
            # Checking if the key exists in the list
            if item[0] == key:
                # If key exists, return its corresponding value
                return item[1]
        # If key is not found, return None
        return None

# Creating an instance of HashMap with the size of flower definitions
blossom = HashMap(len(flower_definitions))
# Assigning each flower name and its meaning to the HashMap
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Retrieving and printing the value for the key 'daisy' from the HashMap
print(blossom.retrieve('daisy'))
# Printing all flower names and their meanings from the flower_definitions list
for i in flower_definitions:
    print(f"{i[0]} + {i[1]}")


# innocence
# begonia + cautiousness
# chrysanthemum + cheerfulness
# carnation + memories
# daisy + innocence
# hyacinth + playfulness
# lavender + devotion
# magnolia + dignity
# morning glory + unrequited love
# periwinkle + new friendship
# poppy + rest
# rose + love
# snapdragon + grace
# sunflower + longevity
# wisteria + good luck