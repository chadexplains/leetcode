class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_count, curr_count, ans = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_count += 1
            else:
                prev_count, curr_count = curr_count, 1
            if prev_count >= curr_count:
                ans += 1
        return ans