#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#5 - Fetch Most Recently Watched Titles:
#We want to implement a feature so that the user can view the n titles that they’ve watched or accessed most recently. You need to come up with a data 
#structure for this feature. Let’s break it down. If we think it through, we realize the following: i) This data structure should maintain titles in order 
#of time since last access; ii) If the data structure is at its capacity, an insertion should replace the least recently accessed item.

from DoublyLinkedList import *

class KVPair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRU_Cache:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.list = DoublyLinkedList()
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache.get(key)
            self.list.move_front(node)
            return node

    def set(self, key, val):
        node = self.cache.get(key, None)
        if node is not None:
            node.data.value = val
            self.list.move_front(node)
            return

        if self.list.size == self.capacity:
            expired = self.list.remove_tail()
            del self.cache[expired.data.key]

        self.cache[key] = self.list.insert_at_head(KVPair(key, val))

    def print_cache(self):
        self.list.print_list()
            


myCache = LRU_Cache(6)

myCache.set(10, 20)
myCache.set(15, 25)
myCache.set(20, 30)
myCache.set(25, 35)
myCache.set(5, 40)
myCache.get(10)
myCache.set(21, 33)
myCache.set(300, 1000)
myCache.print_cache()

