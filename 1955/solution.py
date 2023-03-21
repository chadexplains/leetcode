class Solution:
    def countSpecialSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                if j == 0 or s[j-1] <= s[i-1]:
                    dp[i] += dp[j]
                    dp[i] %= 1000000007
        return dp[n]