class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    # def insertToHead(self, key, value):
    #     temp = HashTableEntry(self.key, self.value)
    #     self.key = key
    #     self.value = value
    #     self.next = temp


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.entries = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return (self.entries / self.capacity)


    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        
        # constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        
        return hash



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        self.entries += 1
        load = self.get_load_factor()
        if load > 0.7:
            self.resize(2 * self.capacity)

        i = self.hash_index(key)
        if self.hash_table[i] is not None:
            newEntry = HashTableEntry(key,value)
            newEntry.next = self.hash_table[i]
            self.hash_table[i] = newEntry
            # print('value over written for', key, 'new value:', self.hash_table[i].value, newEntry.value)
        else:
            self.hash_table[i] = HashTableEntry(key,value)

        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        
        i = self.hash_index(key)
        found = False
        node = self.hash_table[i]
        prev = HashTableEntry(None, None)

        if node.next is None and node.key == key:
            self.hash_table[i] = None
            found = True

        while not found and node is not None:
            if node.key == key:
                if node.next is not None:
                    prev.next = node.next
                    node = node.next
                found = True
            else:
                prev = node
                node = node.next
        
        if found:
            self.entries -= 1
            if self.get_load_factor() < 0.2:
                new_capacity = 0.5 * self.capacity
                if new_capacity > 8:
                    self.resize(new_capacity)
                else:
                    self.resize(8)
            return
        else:
            print('Key not found')
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        node = self.hash_table[i]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        resized = HashTable(new_capacity)

        for entry in self.hash_table:
            if entry is not None:
                node = entry
                entries = []
                while node:
                    entries.append([node.key, node.value])
                    node = node.next
                i = len(entries) - 1
                while i >= 0:
                    resized.put(entries[i][0], entries[i][1])
                    i -= 1

        self.capacity = new_capacity
        self.hash_table = resized.hash_table
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
