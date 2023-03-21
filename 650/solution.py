class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break
        return dp[n]