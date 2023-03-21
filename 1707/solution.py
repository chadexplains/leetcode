class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (1 << maximumBit) - 1
        res = []
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            res.append(xor_sum ^ max_val)
        return res[::-1]