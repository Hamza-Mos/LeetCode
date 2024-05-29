"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])

        while queue:
            currLevelLen = len(queue)

            for i in range(currLevelLen - 1):
                currNode = queue.popleft()
                currNode.next = queue[0]

                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)


            lastNode = queue.popleft()

            if lastNode.left:
                queue.append(lastNode.left)

            if lastNode.right:
                queue.append(lastNode.right)

            lastNode.next = None

        return root
        