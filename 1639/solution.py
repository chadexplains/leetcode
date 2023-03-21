class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(target), len(words[0])
        dp = [[0] * len(words) for _ in range(n)]
        mod = 10**9 + 7
        for j in range(len(words)):
            dp[0][j] = sum([1 for c in words[j] if c == target[0]])
        for i in range(1, n):
            for j in range(len(words)):
                dp[i][j] = sum([dp[i-1][k] for k in range(len(words)) if words[j][i] == target[i] and words[j][:i] == words[k][:i]]) % mod
        return sum(dp[-1]) % mod