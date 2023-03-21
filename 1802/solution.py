class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            l = max(mid - index, 0)
            r = max(mid - (n - 1 - index), 0)
            total = (mid * (mid + 1)) // 2
            total -= ((l * (l + 1)) // 2)
            total -= ((r * (r + 1)) // 2)
            total += max(0, l + r - mid + 1) * mid
            if total <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left