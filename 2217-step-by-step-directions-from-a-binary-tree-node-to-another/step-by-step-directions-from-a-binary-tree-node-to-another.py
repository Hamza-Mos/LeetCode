# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # convert tree to graph
        adjList = defaultdict(list)

        def createGraph(node, parent):
            if not node:
                return

            # connect node to parent
            if parent:
                adjList[node.val].append((parent.val, 'U'))

            # connect node to children
            if node.left:
                adjList[node.val].append((node.left.val, 'L'))

            if node.right:
                adjList[node.val].append((node.right.val, 'R'))

            # dfs on children
            createGraph(node.left, node)
            createGraph(node.right, node)

        createGraph(root, None)

        # do a bfs from startValue to destValue
        queue = deque([(startValue, "")]) # each element contains [start value, directions string]
        visited = set()

        while queue:
            node, directions = queue.popleft()

            if node == destValue:
                return directions

            if node in visited:
                continue

            visited.add(node)

            # visit neighbouring nodes
            for nextNode, nextDirection in adjList[node]:
                if nextNode not in visited:
                    queue.append((nextNode, directions + nextDirection))

        return -1
        