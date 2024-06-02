# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def dfs(node):
            if not node:
                return 0

            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            self.maxPath = max(self.maxPath, leftPath + rightPath + node.val)

            return max(leftPath + node.val, rightPath + node.val, 0)

        dfs(root)
        return self.maxPath
        