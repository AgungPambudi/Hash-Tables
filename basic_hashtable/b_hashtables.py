

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max_val):
    result = 5381
    for c in string:
        result = (result * 33) + ord(c)
    return result % max_val


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    i = hash(key, hash_table.capacity)
    element = Pair(key, value)
    existing = hash_table.storage[i]

    if existing is not None:
        print(f'Warning: overwriting key at index {i}')
    
    hash_table.storage[i] = element



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    i = hash(key, hash_table.capacity)
    existing = hash_table.storage[i]
    
    if existing is None:
        print(f'Warning: {key} not in hash table')
    
    else:
        hash_table.storage[i] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    i = hash(key, hash_table.capacity)
    element = hash_table.storage[i]

    return element.value if element is not None else None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
