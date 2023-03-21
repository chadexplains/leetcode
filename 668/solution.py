class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(mid):
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid // i, n)
            return cnt
        left, right = 1, m*n
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left