class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, float('inf'), float('-inf')
            left_size, left_min, left_max = dfs(node.left)
            right_size, right_min, right_max = dfs(node.right)
            if left_size == -1 or right_size == -1 or not left_max < node.val < right_min:
                return -1, 0, 0
            size = left_size + right_size + 1
            return size, min(left_min, node.val), max(right_max, node.val)
        return dfs(root)[0] if root else 0