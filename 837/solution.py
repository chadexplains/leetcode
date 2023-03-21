class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (K + W)
        window_sum = 0.0
        for i in range(K, K + W):
            dp[i] = 1.0
            window_sum += 1.0
        for i in range(K - 1, -1, -1):
            dp[i] = window_sum / W
            window_sum -= dp[i + W]
            window_sum += dp[i]
        return sum(dp[:N+1])