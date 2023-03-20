class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if not self.first and self.prev.val >= node.val:
            self.first = self.prev
        if self.first and self.prev.val >= node.val:
            self.second = node
        self.prev = node
        self.inorder(node.right)