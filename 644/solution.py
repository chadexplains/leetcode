class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = min(nums), max(nums)
        while r - l > 1e-5:
            mid = (l + r) / 2
            if self.check(nums, mid, k):
                l = mid
            else:
                r = mid
        return l
    
    def check(self, nums, mid, k):
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i] - mid)
        min_prefix = 0
        for j in range(k, len(nums) + 1):
            if prefix[j] - min_prefix >= 0:
                return True
            min_prefix = min(min_prefix, prefix[j - k + 1])
        return False