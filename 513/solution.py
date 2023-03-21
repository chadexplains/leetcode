class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        leftmost_value = root.val
        current_depth = 0
        while queue:
            node, depth = queue.pop(0)
            if depth > current_depth:
                current_depth = depth
                leftmost_value = node.val
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return leftmost_value