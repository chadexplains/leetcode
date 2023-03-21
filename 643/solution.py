class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = max_sum = sum(nums[:k])
        for i in range(k, n):
            sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, sum)
        return max_sum/k