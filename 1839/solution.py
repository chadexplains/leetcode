class Solution:
    def longestBeautifulSubstring(self, s: str) -> int:
        vowels = "aeiou"
        left = right = 0
        longest = 0
        while right < len(s):
            if s[right] == vowels[0]:
                while right < len(s) and s[right] == vowels[0]:
                    right += 1
                if left > 0 and s[left-1] == vowels[4]:
                    longest = max(longest, right - left)
                left = right
            elif s[right] == vowels[1] and left > 0 and s[left-1] == vowels[0]:
                right += 1
            elif s[right] == vowels[2] and left > 0 and s[left-1] == vowels[1]:
                right += 1
            elif s[right] == vowels[3] and left > 0 and s[left-1] == vowels[2]:
                right += 1
            elif s[right] == vowels[4] and left > 0 and s[left-1] == vowels[3]:
                right += 1
            else:
                left = right
            
        if left > 0 and s[left-1] == vowels[4]:
            longest = max(longest, right - left)
        return longest