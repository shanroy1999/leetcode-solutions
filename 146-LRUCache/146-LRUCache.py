class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity      # Max number of keys cache can hold
        self.cache = {}               # Hash map Store key-value pairs

        # Keep track of order of the key usage using Doubly linked list
        # allow O(1) insertion and deletion at both ends
        # move recently used keys to the front and least recently used keys at the back
        self.head = Node()      # Most recently used
        self.tail = Node()      # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove node from the linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_to_front(self, node):
        # Add node to the front of the linked list
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # If key exists, move node to front of the list, and return the value
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)      # Remove current position
            self._add_to_front(node)   # Move to the front - most recently used
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # If key exists -> update value and move node to the front
        if key in self.cache:
            node = self.cache[key]
            node.value = value    # Update the value
            self._remove(node)    # Remove the current position
            self._add_to_front(node)   # Move to the front - most recently used
        else:
        # If key doesn't exists -> If cache is full -> remove least recently used node
        #                       -> Add new node to the front and update the hash map
            if len(self.cache) >= self.capacity:
                # Remove the least recently used node (from the tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            # Add the new node to the front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
