class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = 0
        deepest_sum = 0
        
        def dfs(node, depth):
            nonlocal max_depth, deepest_sum
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                deepest_sum = node.val
            elif depth == max_depth:
                deepest_sum += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return deepest_sum