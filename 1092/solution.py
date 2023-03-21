def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i, j = m, n
        result = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result = str1[i-1] + result
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                result = str1[i-1] + result
                i -= 1
            else:
                result = str2[j-1] + result
                j -= 1
        if i > 0:
            result = str1[:i] + result
        if j > 0:
            result = str2[:j] + result
        return result