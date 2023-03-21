class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_map = {0: -1}
        max_len = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in sum_map:
                max_len = max(max_len, i - sum_map[sum - k])
            if sum not in sum_map:
                sum_map[sum] = i
        return max_len