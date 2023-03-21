class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if k - node.val in values:
                return True
            values.add(node.val)
            node = node.right
        return False