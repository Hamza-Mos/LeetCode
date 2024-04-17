# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder can be used to build the tree
        # inorder tells you where the node is (left or right) and when to end

        self.inorderIndices = { val : index for index, val in enumerate(inorder) }
        self.index = 0 # index for preorder traversal

        def dfs(lowerBoundIndex, upperBoundIndex):
            # this subtree ends here (bounds are invalid)
            if lowerBoundIndex > upperBoundIndex:
                return None

            currNode = TreeNode(preorder[self.index])
            inorderIndex = self.inorderIndices[preorder[self.index]]

            self.index += 1

            currNode.left = dfs(lowerBoundIndex, inorderIndex - 1)
            currNode.right = dfs(inorderIndex + 1, upperBoundIndex)

            return currNode

        return dfs(0, len(inorder) - 1)
            
        