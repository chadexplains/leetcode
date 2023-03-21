def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = float('inf')
            for x in range(i):
                dp[i][j] = min(dp[i][j], dp[x][j-1] + max(nums[x+1:i+1]) - min(nums[x+1:i+1]))
    return dp[n][k]