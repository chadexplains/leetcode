class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        vowel_map = {v: i for i, v in enumerate(vowels)}
        counts = [0] * 32
        counts[0] = 1
        result = 0
        mask = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= 1 << vowel_map[c]
            if counts[mask] != 0:
                result = max(result, i + 1 - counts[mask])
            else:
                counts[mask] = i + 1
        return result