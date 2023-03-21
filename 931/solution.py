class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = A[0][j]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])