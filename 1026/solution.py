```def maxAncestorDiff(self, root: TreeNode, mn=float('inf'), mx=float('-inf')) -> int:
    if not root:
        return 0
    mx = max(mx, root.val)
    mn = min(mn, root.val)
    return max(abs(mx - root.val), abs(mn - root.val), self.maxAncestorDiff(root.left, mn, mx), self.maxAncestorDiff(root.right, mn, mx))```