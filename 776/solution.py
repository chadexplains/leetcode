```def splitBST(root, V):
    if not root:
        return [None, None]
    elif root.val <= V:
        res = splitBST(root.right, V)
        root.right = res[0]
        return [root, res[1]]
    else:
        res = splitBST(root.left, V)
        root.left = res[1]
        return [res[0], root]```