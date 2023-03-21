class Solution:
    def minOperationsToFlip(self, s: str, x: int, exp: str) -> int:
        n = len(s)
        dp = [[float('inf')] * (x+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(x+1):
                for k in range(i-1, -1, -1):
                    val = int(s[k:i])
                    if j-val >= 0:
                        dp[i][j] = min(dp[i][j], dp[k][j-val] + (i-k-1))
                    if j+val <= x:
                        dp[i][j] = min(dp[i][j], dp[k][j+val] + (i-k-1))
        return dp[n][x]