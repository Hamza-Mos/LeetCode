# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            leftPathSum = dfs(node.left)
            rightPathSum = dfs(node.right)

            currPathSum = node.val + leftPathSum + rightPathSum
            self.maxSum = max(self.maxSum, currPathSum)

            return max(max(leftPathSum, rightPathSum) + node.val, 0)

        dfs(root)

        return self.maxSum
        