class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, max(ribbons)
        while l <= r:
            mid = (l + r) // 2
            pieces = sum(r // mid for r in ribbons)
            if pieces >= k:
                l = mid + 1
            else:
                r = mid - 1
        return r