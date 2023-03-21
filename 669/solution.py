def trimBST(root, L, R):
    if not root:
        return None
    if root.val < L:
        return trimBST(root.right, L, R)
    if root.val > R:
        return trimBST(root.left, L, R)
    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)
    return root