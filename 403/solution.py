class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        for stone in stones:
            for jump in dp[stone]:
                for k in range(jump - 1, jump + 2):
                    if k > 0 and stone + k in dp:
                        dp[stone + k].add(k)
        return len(dp[stones[-1]]) > 0