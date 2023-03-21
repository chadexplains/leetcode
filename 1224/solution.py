class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = collections.Counter()
        freq_freq = collections.Counter()
        res = 0
        for i, num in enumerate(nums):
            freq[num] += 1
            freq_freq[freq[num]] += 1
            if freq[num] * freq_freq[freq[num]] == i + 1 and i != len(nums) - 1:
                res = i + 2
            elif freq[num] * freq_freq[freq[num]] == i and i != len(nums) - 1:
                res = i + 1
            elif freq_freq[1] == 1 and freq_freq[freq[num] - 1] == i and i != len(nums) - 1:
                res = i + 1
            elif freq_freq[1] == i + 1:
                res = i + 1
        return res