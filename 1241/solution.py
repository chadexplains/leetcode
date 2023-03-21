class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if l == 1:
                    dp[i][j] = 1
                elif l == 2:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = l + min(dp[i][k] + dp[k+1][j] for k in range(i, j) if arr[k] != arr[j])
                    if arr[i] == arr[j]:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + dp[j][j])
        return dp[0][n-1]