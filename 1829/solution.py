class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_num = (1 << maximumBit) - 1
        xor_sum = reduce(xor, nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = xor_sum ^ max_num
            xor_sum ^= nums[n - i - 1]
        return ans