class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i] = 1
        for i in range(n+1):
            for j in range(i+1, n+1):
                for k in range(i+1, j):
                    dp[i][j] += dp[i][k-1] * dp[k][j-1]
                    dp[i][j] %= 10**9 + 7
        return dp[0][n]