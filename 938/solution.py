class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return curr_sum
            if node.val < L:
                return dfs(node.right, curr_sum)
            if node.val > R:
                return dfs(node.left, curr_sum)
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum) + node.val
        return dfs(root, 0)