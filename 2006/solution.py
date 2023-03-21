class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for num in nums:
            if num + k in freq:
                count += freq[num + k]
            if num - k in freq:
                count += freq[num - k]
            freq[num] = freq.get(num, 0) + 1
        return count