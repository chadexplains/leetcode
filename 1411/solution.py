class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i in range(len(nums)) if nums[i] == 1]
        n = len(ones)
        if n < k:
            return -1
        mid = k // 2
        ans = float('inf')
        for i in range(n - k + 1):
            j = i + k - 1
            left = i
            right = j
            res = 0
            for p in range(mid):
                res += ones[mid] - ones[left] - (mid - p)
                res += ones[right] - ones[mid] - (p - 0)
                left += 1
                right -= 1
            ans = min(ans, res)
        return ans