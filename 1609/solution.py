class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        q = [root]
        level = 0
        while q:
            size = len(q)
            prev = None if level % 2 == 0 else float('inf')
            for i in range(size):
                node = q.pop(0)
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev is not None and node.val <= prev):
                        return False
                else:
                    if node.val % 2 == 1 or (prev is not None and node.val >= prev):
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True