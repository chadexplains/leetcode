class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallest = '~'
        def dfs(node, path):
            if not node:
                return
            path = chr(node.val + 97) + path
            if not node.left and not node.right:
                self.smallest = min(self.smallest, path)
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, '')
        return self.smallest