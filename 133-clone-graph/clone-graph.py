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
            
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            oldToNew[node] = Node(node.val)

            for neighbor in node.neighbors:
                oldToNew[node].neighbors.append(dfs(neighbor))

            return oldToNew[node]

        return dfs(node)
        