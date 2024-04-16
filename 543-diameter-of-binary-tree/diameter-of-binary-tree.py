# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def dfs(node):
            if not node:
                return 0

            leftDiam = dfs(node.left)
            rightDiam = dfs(node.right)

            currDiam = leftDiam + rightDiam
            self.maxDiam = max(self.maxDiam, currDiam)

            return max(leftDiam, rightDiam) + 1

        dfs(root)

        return self.maxDiam
        