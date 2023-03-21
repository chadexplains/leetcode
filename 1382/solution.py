```def balanceBST(self, root: TreeNode) -> TreeNode:
    def inorder(node):
        return inorder(node.left) + [node] + inorder(node.right) if node else []
    def buildTree(nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = nodes[mid]
        root.left = buildTree(nodes[:mid])
        root.right = buildTree(nodes[mid+1:])
        return root
    nodes = inorder(root)
    return buildTree(nodes)```