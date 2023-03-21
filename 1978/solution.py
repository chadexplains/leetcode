class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        for i in range(2**n):
            binary = bin(i)[2:].zfill(n)
            if binary not in nums:
                return binary