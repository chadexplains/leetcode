class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] * 2
                    l, r = i+1, j-1
                    while l <= r and s[l] != s[i]:
                        l += 1
                    while l <= r and s[r] != s[i]:
                        r -= 1
                    if l == r:
                        dp[i][j] += 1
                    elif l > r:
                        dp[i][j] += 2
                    else:
                        dp[i][j] -= dp[l+1][r-1]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
        return dp[0][n-1]