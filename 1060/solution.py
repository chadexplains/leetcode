class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(idx):
            return nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing(left - 1)