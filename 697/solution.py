class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = [1, i, i]
            else:
                freq[num][0] += 1
                freq[num][2] = i
            max_freq = max(max_freq, freq[num][0])
        min_len = len(nums)
        for key, value in freq.items():
            if value[0] == max_freq:
                min_len = min(min_len, value[2] - value[1] + 1)
        return min_len