class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        odd_count = 0
        for count in freq.values():
            if count % 2 == 1:
                odd_count += 1
        return odd_count <= 1
