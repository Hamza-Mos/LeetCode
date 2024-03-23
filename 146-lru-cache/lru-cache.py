class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.key = key
        self.value = value

class LRUCache:
    # constructor
    def __init__(self, capacity):
        self.capacity = capacity
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    # removes a key,value pair from the list
    def remove(self, key):
        nodeToRemove = self.cache[key]
        prevNode, nextNode = nodeToRemove.prev, nodeToRemove.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        del self.cache[key]

    # inserts a key, value pair into the list
    def insert(self, key, value):
        nodeToInsert = Node(key, value)
        prevNode, nextNode = self.right.prev, self.right

        prevNode.next = nodeToInsert
        nextNode.prev = nodeToInsert

        nodeToInsert.next = nextNode
        nodeToInsert.prev = prevNode

        self.cache[key] = nodeToInsert


    def get(self, key):
        if key in self.cache:
            value = self.cache[key].value
            self.remove(key)
            self.insert(key, value)
            return self.cache[key].value
        
        return -1
    
    def put(self, key, value):
        # edge case: key is already in our list
        if key in self.cache:
            self.remove(key)

        # insert key, value into cache
        self.insert(key, value)

        # remove the LRU node if we are above capacity
        if len(self.cache) > self.capacity:
            lruNode = self.left.next
            self.remove(lruNode.key)