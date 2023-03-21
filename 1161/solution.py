class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = {}
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if level in level_sum:
                level_sum[level] += node.val
            else:
                level_sum[level] = node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return max(level_sum, key=level_sum.get)