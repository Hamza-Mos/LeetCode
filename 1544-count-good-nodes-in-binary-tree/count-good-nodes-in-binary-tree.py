# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, maxSeenSoFar):
            if not node:
                return

            if node.val >= maxSeenSoFar:
                self.count += 1
                maxSeenSoFar = node.val

            dfs(node.left, maxSeenSoFar)
            dfs(node.right, maxSeenSoFar)

        dfs(root, float('-inf'))

        return self.count
        