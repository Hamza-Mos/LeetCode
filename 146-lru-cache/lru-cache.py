class ListNode:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # maps key to node
        self.capacity = capacity
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    # helper functions
    def insert(self, key, value):
        newNode = ListNode(key, value)
        self.cache[key] = newNode

        prevNode = self.right.prev
        prevNode.next = newNode
        self.right.prev = newNode
        newNode.next = self.right
        newNode.prev = prevNode

    def remove(self, key):
        nodeToRemove = self.cache[key]
        del self.cache[key] # remove from cache

        prevNode, nextNode = nodeToRemove.prev, nodeToRemove.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        value = node.value
        self.remove(key)
        self.insert(key, value)

        return value
        

    def put(self, key: int, value: int) -> None:
        # case that key exists
        if key in self.cache:
            self.remove(key)
            self.insert(key, value)
            return

        self.insert(key, value)

        if len(self.cache) > self.capacity:
            self.remove(self.left.next.key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)