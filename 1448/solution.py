class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            nonlocal count
            if not node:
                return
            if node.val >= max_val:
                count += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        count = 0
        dfs(root, float('-inf'))
        return count