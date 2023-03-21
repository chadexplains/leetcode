def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
    def helper(node, v, d, depth):
        if not node:
            return
        if depth == d - 1:
            left, right = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left, node.right.right = left, right
        else:
            helper(node.left, v, d, depth + 1)
            helper(node.right, v, d, depth + 1)
        return node
    if d == 1:
        new_root = TreeNode(v)
        new_root.left = root
        return new_root
    helper(root, v, d, 1)