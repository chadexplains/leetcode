class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for num in nums:
            if k - num in freq and freq[k - num] > 0:
                freq[k - num] -= 1
                count += 1
            else:
                freq[num] = freq.get(num, 0) + 1
        return count