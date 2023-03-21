class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node):
            nonlocal sum
            if not node:
                return
            reverse_inorder(node.right)
            sum += node.val
            node.val = sum
            reverse_inorder(node.left)
        sum = 0
        reverse_inorder(root)
        return root