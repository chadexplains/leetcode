def removeLeafNodes(root: TreeNode, target: int) -> TreeNode:
    if root is None:
        return None
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if root.left is None and root.right is None and root.val == target:
        return None
    return root