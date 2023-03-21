def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    idx_map = {val:idx for idx, val in enumerate(inorder)}
    def helper(left, right):
        if left > right:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        idx = idx_map[val]
        root.right = helper(idx+1, right)
        root.left = helper(left, idx-1)
        return root
    return helper(0, len(inorder)-1)