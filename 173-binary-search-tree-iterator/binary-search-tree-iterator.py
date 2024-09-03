# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = 0
        self.tree = []
        self.initialize_tree(root)

    def initialize_tree(self, root):
        if not root:
            return

        self.initialize_tree(root.left)
        self.tree.append(root.val)
        self.initialize_tree(root.right)
        

    def next(self) -> int:
        self.index += 1
        return self.tree[self.index - 1]
        

    def hasNext(self) -> bool:
        return self.index < len(self.tree)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()