```class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal curr
            if not node:
                return
            inorder(node.left)
            node.left = None
            curr.right = node
            curr = node
            inorder(node.right)
        ans = curr = TreeNode(None)
        inorder(root)
        return ans.right```