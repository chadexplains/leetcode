class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-1] * (target + 1)
        dp[0] = 0
        for i in range(len(cost)):
            for j in range(cost[i], target + 1):
                if dp[j - cost[i]] != -1:
                    dp[j] = max(dp[j], dp[j - cost[i]] * 10 + i + 1)
        if dp[target] == -1:
            return "0"
        return str(dp[target])