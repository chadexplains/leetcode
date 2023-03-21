```def delNodes(root, to_delete):
    to_delete_set = set(to_delete)
    res = []
    def helper(node, is_root):
        if not node:
            return None
        if node.val in to_delete_set:
            node.left = helper(node.left, True)
            node.right = helper(node.right, True)
            return None
        else:
            if is_root:
                res.append(node)
            node.left = helper(node.left, False)
            node.right = helper(node.right, False)
            return node
    helper(root, True)
    return res```