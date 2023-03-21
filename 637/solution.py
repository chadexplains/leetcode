class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        result = []
        while queue:
            level_sum = 0
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_size)
        return result