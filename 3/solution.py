class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_len = max(max_len, len(char_set))
            else:
                char_set.remove(s[left])
                left += 1
        return max_len