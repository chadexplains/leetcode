class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right, ans = 1, 10**6, 0
        while left <= right:
            mid = (left + right) // 2
            apples = 2 * mid * (mid + 1) * (2 * mid + 1)
            if apples >= neededApples:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans * 8