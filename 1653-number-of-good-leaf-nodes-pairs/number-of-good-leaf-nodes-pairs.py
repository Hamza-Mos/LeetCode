# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        # array[i] = number of nodes at a distance[i]
        def dfs(node):
            # null
            if not node:
                return [0] * (distance + 1)

            # leaf node
            if not node.left and not node.right:
                result = [0] * (distance + 1)
                result[0] = 1 # leaf node is at a distance 0 from itself
                return result

            leftSubTree = dfs(node.left)
            rightSubTree = dfs(node.right)

            currNode = [0] * (distance + 1)

            # distance shifts by 1 as you go up the tree to the parent
            for i in range(distance):
                currNode[i + 1] = leftSubTree[i] + rightSubTree[i]

            prefixSum = 0 # number of good leaf nodes found from this point
            index1 = distance - 2 # max distance from left subtree

            prefixSum = 0
            index2 = 0
            for index1 in range(distance - 2, -1, -1):
                prefixSum += rightSubTree[index2]
                self.res += prefixSum * leftSubTree[index1]
                index2 += 1

            return currNode

        dfs(root)
        return self.res

