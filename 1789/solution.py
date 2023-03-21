class Solution:
    def maxCoins(self, coins: List[int], k: int) -> int:
        dp = [0] * k
        dp[0] = 1
        for coin in coins:
            for i in range(k - 1, -1, -1):
                dp[(i + coin) % k] = max(dp[(i + coin) % k], dp[i] + (i + coin) // k)
        return dp[0]