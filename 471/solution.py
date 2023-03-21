class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [[s[i] for i in range(n)] for j in range(n)]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                substr = s[i:j+1]
                dp[i][j] = substr
                if l > 4:
                    for k in range(i, j):
                        if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                else:
                    continue
                for k in range(1, l):
                    repeat = l // k
                    if repeat * k == l and substr == substr[:k] * repeat:
                        encoded = str(repeat) + '[' + dp[i][i+k-1] + ']'
                        if len(encoded) < len(dp[i][j]):
                            dp[i][j] = encoded
        return dp[0][n-1]