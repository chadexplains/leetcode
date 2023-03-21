class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely_nodes = []
        def dfs(node, parent):
            if not node:
                return
            if parent and (not node.left or not node.right):
                lonely_nodes.append(node.left.val if node.left else node.right.val)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        return lonely_nodes