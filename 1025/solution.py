class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N+1)
        dp[0] = False
        dp[1] = False
        for i in range(2, N+1):
            for j in range(1, i//2+1):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
                    break
        return dp[N]