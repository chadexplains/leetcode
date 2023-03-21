class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely_nodes = []
        def dfs(node):
            if not node:
                return
            if node.left and not node.right:
                lonely_nodes.append(node.left.val)
            if node.right and not node.left:
                lonely_nodes.append(node.right.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return lonely_nodes