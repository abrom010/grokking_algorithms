'''
What is a hash map? It's a data structure. It's good for looking up values. The average
time for search is O(1). Worst case, it's O(n). It is like a dictionary, it holds keys
and values. It can be implemented using an array and hash function combo. The hash
function takes a key and returns a value, consistently. For example, "apple" might always
return the number 4. A collision happens when two different keys return the same value in that
hash function. A work-around is to use a linked list for the corresponding slot in the array.
Now the array slot can have multiple values, that can be found through a search in that linked list.
Depending on the shape of our hash map, the operations can vary in efficiency. For example, if
a majority of entries end up in the same slot of our array (because our hash function didn't do a very
good job of spreading them out), the lookup time with be very linear, since it's basically a linked list
search. "Load factor" is the ratio of total entries to total slots. Collisions are best avoided when
maintaining a low load factor, and utilizing a good hash function.
'''

# example of a hash map implemented in python
class HashTable:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
 
    # Remove a value with specific key
    def delete_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
 
 
hash_table = HashTable(50)
 
# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()
 
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
 
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
 
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)