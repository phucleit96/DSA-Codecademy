class HashMap:
    def __init__(self, array_size):
        # Initializing the HashMap with a specified array size and creating an array with 'None' values.
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def hash(self, key, count_collisions=0):
        # Generating a hash code for the provided key using its bytes and summing them up.
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions  # Adding collision count to the hash code

    def compressor(self, hash_code):
        # Applying modulo to the hash code to compress it within the range of the array size.
        return hash_code % self.array_size

    def assign(self, key, value):
        # Assigning a value to a specific key in the HashMap
        array_index = self.compressor(self.hash(key))  # Getting the index in the array
        current_array_value = self.array[array_index]

        if current_array_value is None:
            # If the slot is empty, assign the key-value pair
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            # If the key already exists, update the value
            self.array[array_index] = [key, value]
            return

        # Collision occurred, handle collision
        number_collisions = 1

        while current_array_value[0] != key:
            # Handle collisions by generating a new hash code and finding a new slot
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                # If an empty slot is found, assign the key-value pair
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                # If the key already exists in a different slot, update the value
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1  # Increment collision count

        return

    def retrieve(self, key):
        # Retrieve the value associated with a given key in the HashMap
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            # If the slot is empty, return None
            return None

        if possible_return_value[0] == key:
            # If the key matches the one in the slot, return its value
            return possible_return_value[1]

        retrieval_collisions = 1

        while possible_return_value != key:
            # Handling collisions during retrieval
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                # If the slot is empty, return None
                return None

            if possible_return_value[0] == key:
                # If the key matches in a different slot, return its value
                return possible_return_value[1]

            retrieval_collisions += 1  # Increment retrieval collision count

        return None

# Creating an instance of HashMap with an array size of 15
hash_map = HashMap(15)

# Assigning key-value pairs to the HashMap
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

# Retrieving and printing values based on keys
print(hash_map.retrieve('gabbro'))    # Output: 'igneous'
print(hash_map.retrieve('sandstone')) # Output: 'sedimentary'
print(hash_map.retrieve('gneiss'))    # Output: 'metamorphic'
