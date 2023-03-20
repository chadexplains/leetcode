class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            if not node.left and not node.right:
                return curr * 10 + node.val
            return dfs(node.left, curr * 10 + node.val) + dfs(node.right, curr * 10 + node.val)
        return dfs(root, 0)