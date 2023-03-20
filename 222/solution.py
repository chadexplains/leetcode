class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    def get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + self.get_height(node.left)