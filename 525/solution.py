class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        running_sum = 0
        sum_index = {0: -1}
        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1
            if running_sum in sum_index:
                max_len = max(max_len, i - sum_index[running_sum])
            else:
                sum_index[running_sum] = i
        return max_len