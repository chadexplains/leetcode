class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        hd = {}
        while queue:
            node, d = queue.pop(0)
            if d not in hd:
                hd[d] = []
            hd[d].append(node.val)
            if node.left:
                queue.append((node.left, d-1))
            if node.right:
                queue.append((node.right, d+1))
        res = []
        for key in sorted(hd.keys()):
            res.append(hd[key])
        return res