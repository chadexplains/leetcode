class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq = {}
        for num in target:
            freq[num] = freq.get(num, 0) + 1
        for num in arr:
            freq[num] = freq.get(num, 0) - 1
        for key in freq:
            if freq[key] != 0:
                return False
        return True