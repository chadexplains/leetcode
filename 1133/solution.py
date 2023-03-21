class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = {}
        for num in A:
            freq[num] = freq.get(num, 0) + 1
        unique_nums = [num for num in freq if freq[num] == 1]
        if not unique_nums:
            return -1
        return max(unique_nums)