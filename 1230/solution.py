class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0] * (target+1)
        dp[0] = 1
        for p in prob:
            for j in range(target, -1, -1):
                dp[j] = dp[j] * (1 - p) + (dp[j-1] if j > 0 else 0) * p
        return dp[target]