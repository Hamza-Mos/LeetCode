# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # preorder traversal

        # leaf node
        if root.val <= 1:
            return True if root.val == 1 else False

        # boolean operator (OR)
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        # boolean operator (AND)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        