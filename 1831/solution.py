class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            l = max(mid - index, 0)
            r = max(mid - (n - 1 - index), 0)
            if (mid * (mid + 1) // 2 - (mid - l) * (mid - l + 1) // 2 - (mid - r) * (mid - r + 1) // 2) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left