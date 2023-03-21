class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x // 2 + 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans