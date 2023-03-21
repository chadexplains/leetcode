class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        result = 0
        has_odd = False
        for count in freq.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                has_odd = True
        if has_odd:
            result += 1
        return result