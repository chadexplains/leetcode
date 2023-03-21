class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        freq = {}
        for num in A:
            if num in freq:
                return num
            else:
                freq[num] = 1
        return -1