class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, key, val):
        prevNode, nextNode = self.right.prev, self.right

        newNode = Node(key, val, nextNode, prevNode)

        prevNode.next = newNode
        self.right.prev = newNode

        self.cache[key] = newNode

    def remove(self, key):
        oldNode = self.cache[key]

        prevNode, nextNode = oldNode.prev, oldNode.next

        prevNode.next, nextNode.prev = nextNode, prevNode

        del self.cache[key]
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(key)
        self.insert(node.key, node.val)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)

        self.insert(key, value)

        if len(self.cache) > self.capacity:
            self.remove(self.left.next.key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)