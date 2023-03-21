def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack1, stack2, res = [root], [], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        res.append(stack2.pop().val)
    return res