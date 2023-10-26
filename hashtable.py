# This is a hashtable implementation in Python.
# Collision resolution is done using chaining.

INITIAL_CAPACITY = 50

class HashTable:
   def __init__(self, size):
      self.capacity = INITIAL_CAPACITY
      self.size = 0
      self.data = [None] * self.capacity
   
   # This is the node class that will be used to create nodes in the linked list for chaining.
   class Node:
      def __init__(self, key, value):
         self.key = key
         self.value = value
         self.next = None

   # The hash function is used to map the key to an index in the array.
   # Receive a key and return an index in the range [0, capacity]
   def hash(self, key):
      hashsum = 0
      for idx, c in enumerate(key):  # iterate over characters in key
         hashsum += (idx + len(key)) ** ord(c) # add weighted value to hashsum
         hashsum = hashsum % self.capacity   # perform modulus to keep hashsum in range
      return hashsum
   
   def insert(self, key, value):
      # 1. Compute index of key
      index = self.hash(key)
      # 2. Go to the node corresponding to the hash
      node = self.data[index]
      # 3. If bucket is empty:
      if node is None:
         # Create node, add it, return
         self.data[index] = self.Node(key, value)
         return
      # 4. If bucket is not empty:
      prev = node
      while node is not None:
         # Check if key already exists
         if node.key == key:
            # If yes, overwrite value
            node.value = value
            return
         prev = node
         node = node.next
         # 5. If key does not exist in bucket:
         # Create node, add it to bucket
         prev.next = self.Node(key, value)
         return
   
   def search(self, key):
      # 1. Compute hash
      index = self.hash(key)
      # 2. Go to first node in list at bucket
      node = self.data[index]
      # 3. Traverse the linked list at this node
      while node is not None and node.key != key:
         node = node.next
      # 4. Now, node is the requested key/value pair or None
      if node is None:
         # Not found
         return None
      else:
         # Found - return the data value
         return node.value
   
   def remove(self, key):
      # 1. Compute hash
      index = self.hash(key)
      node = self.data[index]
      prev = None
      # 2. Iterate to requested node
      while node is not None and node.key != key:
         prev = node
         node = node.next
      # Now, node is either the requested node or none
      if node is None:
         # 3. Key not found
         return None
      else:
         # 4. The key was found.
         self.size -= 1
         result = node.value
         # Delete this element in linked list
         if prev is None:
            self.data[index] = node.next # May be None, or the next match
         else:
            prev.next = prev.next.next # LinkedList delete by skipping over
      
      return result
