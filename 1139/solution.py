class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
                    if dp[i][j] >= 1:
                        for k in range(dp[i][j], 0, -1):
                            if i >= k - 1 and j >= k - 1 and dp[i][j-k+1] >= k and dp[i-k+1][j] >= k:
                                max_area = max(max_area, k * k)
        return max_area