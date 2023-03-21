class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        if self.check(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def check(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.check(head.next, root.left) or self.check(head.next, root.right)