class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        res = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j < n:
            if nums[j] >= nums[i]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res