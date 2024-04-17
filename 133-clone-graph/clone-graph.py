"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        oldNodeToNewNode = {}

        def getClones(currNode):
            # check if node was already visited
            if currNode in oldNodeToNewNode:
                return

            oldNodeToNewNode[currNode] = Node(currNode.val)

            for nextNode in currNode.neighbors:
                getClones(nextNode)
                oldNodeToNewNode[currNode].neighbors.append(oldNodeToNewNode[nextNode])

        # populate map
        getClones(node)

        return oldNodeToNewNode[node]
            

        