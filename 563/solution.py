class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0
        def sum_and_tilt(node):
            if not node:
                return 0
            left_sum = sum_and_tilt(node.left)
            right_sum = sum_and_tilt(node.right)
            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt
            return left_sum + right_sum + node.val
        sum_and_tilt(root)
        return self.total_tilt