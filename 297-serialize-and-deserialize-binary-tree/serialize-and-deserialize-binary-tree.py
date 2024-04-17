# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []

        def dfs(node):
            if not node:
                nodes.append("N")
                return

            nodes.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(nodes)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "N":
                self.index += 1
                return None

            currNode = TreeNode(nodes[self.index])
            self.index += 1
            currNode.left = dfs()
            currNode.right = dfs()

            return currNode

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))