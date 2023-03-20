class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))
        if not root:
            return []
        paths = []
        dfs(root, str(root.val))
        return paths