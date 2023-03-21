class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        remainder_dict = {0: -1}
        cumulative_sum = 0
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            remainder = cumulative_sum % k
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] >= 2:
                    return True
            else:
                remainder_dict[remainder] = i
        return False