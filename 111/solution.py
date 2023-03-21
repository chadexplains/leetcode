class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if not root.left or not root.right:
            return left_depth + right_depth + 1
        return min(left_depth, right_depth) + 1