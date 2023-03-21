```class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for j in range(n+1):
            dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, n+1):
                if S[i-1] == 'D':
                    dp[i][j] = sum(dp[i-1][k] for k in range(j, i))
                else:
                    dp[i][j] = sum(dp[i-1][k] for k in range(j-1))
        return sum(dp[-1]) % (10**9 + 7)```