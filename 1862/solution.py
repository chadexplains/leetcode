class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += 1
        prefix_sum = freq.copy()
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        result = 0
        for num in nums:
            for i in range(1, (max(nums) // num) + 1):
                result += (prefix_sum[i * num - 1] - prefix_sum[(i - 1) * num - 1]) * i * freq[num]
        return result % MOD