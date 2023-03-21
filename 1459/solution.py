def minimumEffort(nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    dp = [[float('inf')] * k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            if j == 0:
                dp[i][j] = wasted_space(0, i)
            else:
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j-1] + wasted_space(p+1, i))
    return dp[n-1][k-1]


def wasted_space(start: int, end: int) -> int:
    return (end - start + 1) * (nums[end] - nums[start]) - sum(nums[start:end+1])