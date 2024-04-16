"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        oldToNew = { None: None }

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            newNode = oldToNew[curr]

            newNode.next = oldToNew[curr.next]
            newNode.random = oldToNew[curr.random]

            curr = curr.next

        return oldToNew[head]
        