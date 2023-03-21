class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            sums.add(total_sum)
            return total_sum
        sums = set()
        total = dfs(root)
        if total % 2 != 0:
            return False
        return total // 2 in sums