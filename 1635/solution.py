class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = 0
        for n in freq.values():
            res += n*(n-1)//2
        return res