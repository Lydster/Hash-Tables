

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
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return (hash & 0xFFFFFFFF) % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    if hash_table.storage[hash(key, hash_table.capacity)] != None and hash_table.storage[hash(key, hash_table.capacity)].key != key:
        print('You are overwriting a value with a different key!')
    hash_table.storage[hash(key, hash_table.capacity)] = Pair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    if hash_table.storage[hash(key, hash_table.capacity)] != None and hash_table.storage[hash(key, hash_table.capacity)].key == key:
        hash_table.storage[hash(key, hash_table.capacity)] = None
    else:
        print("You tried to remove a value that is not there.")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    if hash_table.storage[hash(key, hash_table.capacity)] != None and hash_table.storage[hash(key, hash_table.capacity)].key == key:
        return hash_table.storage[hash(key, hash_table.capacity)].value
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
