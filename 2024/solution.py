class Solution:
    def maxConsecutiveAnswers(self, s: str) -> int:
        i = 0
        max_confusion = 0
        for j in range(len(s)):
            if j > 0 and s[j] == s[j-1]:
                continue
            while i < j and j-i > max_confusion:
                i += 1
            while i < j and s[i] == s[j]:
                i += 1
            max_confusion = max(max_confusion, j-i+1)
        return max_confusion