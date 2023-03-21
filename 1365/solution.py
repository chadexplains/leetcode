class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
        prefix_sum = [0] * 101
        for i in range(1, 101):
            prefix_sum[i] = prefix_sum[i-1] + freq[i-1]
        res = []
        for num in nums:
            res.append(prefix_sum[num])
        return res