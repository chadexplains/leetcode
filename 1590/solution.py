class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        remainder_to_index = {0: 0}
        min_length = float('inf')
        for i, prefix in enumerate(prefix_sum):
            remainder = prefix % p
            complement = (remainder - target) % p
            if complement in remainder_to_index:
                length = i - remainder_to_index[complement]
                min_length = min(min_length, length)
            remainder_to_index[remainder] = i
        return min_length if min_length < len(nums) else -1