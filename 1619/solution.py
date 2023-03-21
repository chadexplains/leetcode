class Solution:
    def trimMean(self, nums: List[int]) -> float:
        n = len(nums)
        to_remove = int(n * 0.05)
        nums.sort()
        return sum(nums[to_remove:n-to_remove]) / (n - 2 * to_remove)