class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        dp = [[[0] * (n+1) for _ in range(P+1)] for _ in range(G+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            for g in range(G+1):
                for p in range(P+1):
                    dp[g][p][i] = dp[g][p][i-1]
                    if g >= group[i-1] and p >= profit[i-1]:
                        dp[g][p][i] += dp[g-group[i-1]][p-profit[i-1]][i-1]
        return sum(dp[g][p][n] for g in range(1, G+1) for p in range(P, -1, -1)) % (10**9 + 7)