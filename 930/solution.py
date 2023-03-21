class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        curr_sum = 0
        sum_count = {0: 1}
        for num in nums:
            curr_sum += num
            if curr_sum - goal in sum_count:
                count += sum_count[curr_sum - goal]
            if curr_sum in sum_count:
                sum_count[curr_sum] += 1
            else:
                sum_count[curr_sum] = 1
        return count