class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_set = set(nodes)
        def dfs(node):
            if not node:
                return None
            if node in nodes_set:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            if left or right:
                return left or right
            return None
        return dfs(root)