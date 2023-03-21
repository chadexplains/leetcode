class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = 0
        curr_vowels = 0
        max_vowels = 0
        for right in range(len(s)):
            if s[right] in vowels:
                curr_vowels += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    curr_vowels -= 1
                left += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels