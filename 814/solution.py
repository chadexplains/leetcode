def pruneTree(root):
    def containsOne(node):
        if not node:
            return False
        left_contains_one = containsOne(node.left)
        right_contains_one = containsOne(node.right)
        if not left_contains_one:
            node.left = None
        if not right_contains_one:
            node.right = None
        return node.val == 1 or left_contains_one or right_contains_one
    return root if containsOne(root) else None