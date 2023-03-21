class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isIdentical(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
        if not s:
            return False
        if isIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)