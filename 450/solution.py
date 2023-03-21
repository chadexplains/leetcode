def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    if root is None:
        return None
    if key < root.val:
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
    return root