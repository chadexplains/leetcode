def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
    queue = [root]
    while queue:
        level_size = len(queue)
        found = False
        for i in range(level_size):
            node = queue.pop(0)
            if found:
                return node
            if node == u:
                found = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if found:
            return None
    return None