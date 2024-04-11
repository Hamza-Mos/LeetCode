# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {0: 1}
        self.pathCount = 0

        def dfs(node, oldSum):
            if not node:
                return

            currPathSum = oldSum + node.val

            pathsToRemove = cache.get(currPathSum - targetSum, 0)
            self.pathCount += pathsToRemove
            cache[currPathSum] = cache.get(currPathSum, 0) + 1

            dfs(node.left, currPathSum)
            dfs(node.right, currPathSum)

            cache[currPathSum] -= 1

        dfs(root, 0)

        return self.pathCount            