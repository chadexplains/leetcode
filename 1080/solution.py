def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
    def dfs(node, curr_sum):
        if not node:
            return None
        curr_sum += node.val
        if not node.left and not node.right:
            return None if curr_sum < limit else node
        node.left = dfs(node.left, curr_sum)
        node.right = dfs(node.right, curr_sum)
        return None if not node.left and not node.right else node
    return dfs(root, 0)