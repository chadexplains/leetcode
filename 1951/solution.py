def minSpaceWastedKResizing(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[float('inf')] * (k+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            max_num = 0
            for l in range(i-1, -1, -1):
                max_num = max(max_num, nums[l])
                dp[i][j] = min(dp[i][j], dp[l][j-1] + (i-l)*max_num - sum(nums[i-1:l:-1]) - max_num)
    return dp[n][k]