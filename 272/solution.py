class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        pred, succ = [], []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < target:
                pred.append(root.val)
            else:
                succ.append(root.val)
            root = root.right
        res = []
        while k:
            if not pred and not succ:
                break
            elif not pred:
                res.append(succ.pop(0))
            elif not succ:
                res.append(pred.pop())
            elif abs(pred[-1] - target) < abs(succ[0] - target):
                res.append(pred.pop())
            else:
                res.append(succ.pop(0))
            k -= 1
        return res