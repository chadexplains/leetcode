class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res