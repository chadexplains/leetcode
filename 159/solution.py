class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        left = right = 0
        max_len = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while len(freq) > 2:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len