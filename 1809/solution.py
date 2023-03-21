class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(n, index, maxSum, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def check(self, n, index, maxSum, mid):
        leftSum = (mid - 1) * mid // 2 if mid > index else (mid - 1 + mid - index) * index // 2 + (mid - index)
        rightSum = (mid - 1) * mid // 2 if mid > n - index - 1 else (mid - 1 + mid - (n - index - 1)) * (n - index - 1) // 2 + (mid - (n - index))
        return leftSum + rightSum + mid <= maxSum