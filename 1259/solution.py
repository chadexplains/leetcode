class Solution:
    def numberOfWays(self, num_people: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * (num_people // 2)
        for i in range(1, num_people // 2 + 1):
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % mod
        return dp[num_people // 2]