class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        left = right = 0
        res = len(s)
        while right < len(s):
            freq[s[right]] -= 1
            while left < len(s) and all(freq[c] <= target for c in 'QWER'):
                res = min(res, right - left + 1)
                freq[s[left]] += 1
                left += 1
            right += 1
        return res