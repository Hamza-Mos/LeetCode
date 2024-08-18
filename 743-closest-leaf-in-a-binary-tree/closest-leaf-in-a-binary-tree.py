# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        adjList = defaultdict(list)
        queue = deque() # for bfs
        visited = set() # for bfs

        # transform tree into a graph
        def dfs(node, parent):
            if not node:
                return

            if node.val == k:
                queue.append(node)

            adjList[node].append(parent)
            adjList[parent].append(node)

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # do bfs
        while queue:
            node = queue.popleft()

            if node.val in visited:
                continue

            # leaf node is found
            if len(adjList[node]) == 1:
                return node.val

            visited.add(node.val)

            # visit children of this node
            for nextNode in adjList[node]:
                if nextNode and nextNode.val not in visited:
                    queue.append(nextNode)

        return -1

