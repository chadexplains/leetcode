```def pathSum(root: TreeNode, sum: int) -> List[List[int]]:
    def dfs(node, target, path):
        if not node:
            return []
        path.append(node.val)
        if not node.left and not node.right and node.val == target:
            res.append(path[:])
        dfs(node.left, target - node.val, path)
        dfs(node.right, target - node.val, path)
        path.pop()
    res = []
    dfs(root, sum, [])
    return res```