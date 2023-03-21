class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        new_s = s + "#" + s[::-1]
        prefix = [0] * len(new_s)
        for i in range(1, len(new_s)):
            j = prefix[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = prefix[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            prefix[i] = j
        return s[len(s) - 1:prefix[-1] - 1:-1] + s