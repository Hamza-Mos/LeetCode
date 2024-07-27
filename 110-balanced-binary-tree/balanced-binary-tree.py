# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(node):
            if not node:
                return 0

            if not self.isBalanced:
                return -1

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            self.isBalanced = self.isBalanced and abs(leftHeight - rightHeight) <= 1

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return self.isBalanced
        