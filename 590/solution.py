class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]