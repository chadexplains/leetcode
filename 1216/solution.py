class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        for kk in range(1, k+1):
            for i in range(n-kk):
                j = i + kk
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        return dp[0][n-1] == 1