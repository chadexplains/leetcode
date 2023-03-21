class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dummy = Node(0, None, None)
        prev = dummy
        def inorder(node):
            nonlocal prev
            if not node:
                return
            inorder(node.left)
            prev.right = node
            node.left = prev
            prev = node
            inorder(node.right)
        inorder(root)
        head = dummy.right
        head.left = prev
        prev.right = head
        return head