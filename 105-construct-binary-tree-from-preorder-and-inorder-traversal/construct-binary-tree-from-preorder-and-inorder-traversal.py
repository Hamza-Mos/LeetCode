# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderIndices = { node: index for index, node in enumerate(inorder) }
        self.preOrderIndex = 0

        def dfs(leftIndex, rightIndex):
            if leftIndex > rightIndex:
                return

            currNode = TreeNode(preorder[self.preOrderIndex])
            self.preOrderIndex += 1

            currNode.left = dfs(leftIndex, inOrderIndices[currNode.val] - 1)
            currNode.right = dfs(inOrderIndices[currNode.val] + 1, rightIndex)

            return currNode

        return dfs(0, len(inorder) - 1)