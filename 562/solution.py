class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m, n = len(M), len(M[0])
        dp = [[0] * 4 for _ in range(n)]
        res = 0
        for i in range(m):
            newDp = [[0] * 4 for _ in range(n)]
            for j in range(n):
                if M[i][j] == 1:
                    newDp[j][0] = dp[j][0] + 1
                    newDp[j][1] = newDp[j - 1][1] + 1 if j > 0 else 1
                    newDp[j][2] = dp[j - 1][2] + 1 if j > 0 else 1
                    newDp[j][3] = dp[j + 1][3] + 1 if j < n - 1 else 1
                    res = max(res, max(newDp[j]))
            dp = newDp
        return res