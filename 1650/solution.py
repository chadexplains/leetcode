```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not p or not q:
            return None
        if p == q:
            return p
        def dfs(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
        return dfs(root, p, q)
```