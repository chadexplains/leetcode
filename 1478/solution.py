class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        for i in range(1, n + 1):
            dp[1][i] = self.calc(houses, 0, i - 1)
        for i in range(2, k + 1):
            for j in range(i, n + 1):
                for l in range(i - 1, j):
                    dp[i][j] = min(dp[i][j], dp[i - 1][l] + self.calc(houses, l, j - 1))
        return dp[k][n]
    
    def calc(self, houses, i, j):
        median = houses[(i + j) // 2]
        return sum(abs(houses[k] - median) for k in range(i, j + 1))