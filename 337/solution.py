class Solution:
    def rob(self, root: TreeNode) -> int:
        def robSubtree(node):
            if not node:
                return (0, 0)
            left, right = robSubtree(node.left), robSubtree(node.right)
            rob_node = node.val + left[1] + right[1]
            rob_children = max(left) + max(right)
            return (rob_node, rob_children)
        return max(robSubtree(root))