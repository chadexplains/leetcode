class Solution:
    def countSpecialSubsequences(self, s: str) -> int:
        dp = [0, 0, 0]
        for c in s:
            if c == '0':
                dp[0] = dp[0] * 2 + 1
            elif c == '1':
                dp[1] = dp[1] * 2 + dp[0]
            else:
                dp[2] = dp[2] * 2 + dp[1]
        return dp[0] % (10**9 + 7)