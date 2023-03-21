class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        cum_sum = 0
        sum_dict = {0: -1}
        for i in range(len(nums)):
            cum_sum += 1 if nums[i] == 1 else -1
            if cum_sum in sum_dict:
                max_len = max(max_len, i - sum_dict[cum_sum])
            else:
                sum_dict[cum_sum] = i
        return max_len