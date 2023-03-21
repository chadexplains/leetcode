def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
    def count(node):
        if not node: return 0
        l, r = count(node.left), count(node.right)
        if node.val == x:
            self.left, self.right = l, r
        return l + r + 1
    count(root)
    return max(max(self.left, self.right), n - self.left - self.right - 1) > n / 2