class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rightmost = {}
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                if depth not in rightmost:
                    rightmost[depth] = node.val
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return [rightmost[depth] for depth in range(max_depth + 1)]