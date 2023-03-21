class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]