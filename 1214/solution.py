class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        values = set()
        def traverse(node):
            if not node:
                return
            values.add(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root1)
        def check(node):
            if not node:
                return False
            if target - node.val in values:
                return True
            return check(node.left) or check(node.right)
        return check(root2)