class Solution:
    def isValidBST(self, root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)