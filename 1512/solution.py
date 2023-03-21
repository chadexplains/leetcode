class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        good_pairs = 0
        for n in freq.values():
            good_pairs += n*(n-1)//2
        return good_pairs