

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max_val):
    result = 5381
    
    for c in string:
        result = ((result << 5)+result)+ord(c)
    
    return result % max_val


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(ht, key, value):
    h_key = hash(key, ht.capacity)
    
    if ht.storage[h_key] == None:
        ht.storage[h_key] = LinkedPair(key, value)
        ht.count += 1
    
    else:
        tmp = ht.storage[h_key]
    
        if tmp.key == key:
            ht.storage[h_key].value = value
            return None
    
        else:
            while tmp.next != None:
                tmp = tmp.next
    
                if tmp.key == key:
                    tmp.value = value
    
                    return None
    
        tmp.next = LinkedPair(key, value)
        ht.count += 1

    if ht.count >= 0.8 * ht.capacity:
        ht = hash_table_resize(ht)
    
    return None


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(ht, key):
    h_key = hash(key, ht.capacity)
    
    if ht.storage[h_key] == None:
        print("WARNING! Deleting a key that does not exist")
        return None
    
    else:
        tmp = ht.storage[h_key]
    
        if tmp.next != None:
            while tmp.next != None:
    
                if tmp.next.key == key:
                    tmp.next = tmp.next.next
                    ht.count -= 1
    
                    if ht.count >= 0.8 * ht.capacity:
                        ht = hash_table_resize(ht)
                    break
    
                tmp = tmp.next
    
        else:
            if tmp.key == key:
                ht.storage[h_key] = None
    
                if ht.count >= 0.8 * ht.capacity:
                    ht = hash_table_resize(ht)
    
                return None
    
    return None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(ht, key):
    addr = hash(key, ht.capacity)
    
    if ht.storage[addr] != None:
        tmp = ht.storage[addr]
    
        while tmp != None:
            if tmp.key == key:
                return tmp.value
            
            tmp = tmp.next
    
    return None


# '''
# Fill this in
# '''
def hash_table_resize(ht):
    if ht.count <= 0.2*ht.capacity:
        new_ht = HashTable(ht.capacity//2)
    
    elif ht.count >= 0.7*ht.capacity:
        new_ht = HashTable(ht.capacity*2)

    if ht.count <= 0.2*ht.capacity or ht.count >= 0.7*ht.capacity:
        for i in range(ht.capacity):
            tmp = ht.storage[i]
    
            if tmp != None:
                while tmp != None:
                    hash_table_insert(new_ht, tmp.key, tmp.value)
                    tmp = tmp.next
    
        ht = new_ht
    
    return ht


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
