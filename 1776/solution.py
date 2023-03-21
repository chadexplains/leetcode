def canPartition(nums):
    n = len(nums)
    s = sum(nums)
    if s % 2 != 0:
        return False
    target = s // 2
    dp = [[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, target+1):
            if j >= nums[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]