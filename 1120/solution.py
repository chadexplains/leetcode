class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(node):
            nonlocal max_avg
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            avg = total_sum / total_count
            max_avg = max(max_avg, avg)
            return total_sum, total_count
        max_avg = float('-inf')
        dfs(root)
        return max_avg