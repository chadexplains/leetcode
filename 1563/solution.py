def stoneGameV(stones: List[int]) -> int:
    n = len(stones)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]
    memo = [[-1] * n for _ in range(n)]
    def dp(start, end):
        if start == end:
            return 0
        if memo[start][end] != -1:
            return memo[start][end]
        result = 0
        for i in range(start, end):
            left_sum = prefix_sum[i] - prefix_sum[start]
            right_sum = prefix_sum[end] - prefix_sum[i]
            if left_sum <= right_sum:
                result = max(result, left_sum + dp(start, i))
            if left_sum >= right_sum:
                result = max(result, right_sum + dp(i + 1, end))
        memo[start][end] = result
        return result
    return dp(0, n - 1)