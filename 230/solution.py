def kthSmallest(root, k):
    def inorder(node):
        nonlocal k
        if not node:
            return None
        left = inorder(node.left)
        if left is not None:
            return left
        k -= 1
        if k == 0:
            return node.val
        right = inorder(node.right)
        return right
    return inorder(root)