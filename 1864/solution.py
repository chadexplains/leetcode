class Solution:
    def minSwaps(self, s: str) -> int:
        ones = s.count('1')
        zeros = s.count('0')
        if abs(ones - zeros) > 1:
            return -1
        if ones > zeros:
            start_with = '1'
        elif ones < zeros:
            start_with = '0'
        else:
            start_with = '0'
        swaps = 0
        for i in range(len(s)):
            if s[i] != start_with:
                swaps += 1
            start_with = '1' if start_with == '0' else '0'
        return swaps // 2