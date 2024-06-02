# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxDiam = 0

        def dfs(node):
            if not node:
                return 0

            leftDiam = dfs(node.left)
            rightDiam = dfs(node.right)

            self.maxDiam = max(self.maxDiam, leftDiam + rightDiam)

            return 1 + max(leftDiam, rightDiam)

        dfs(root)

        return self.maxDiam
        