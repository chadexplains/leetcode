def minOperations(self, target: List[int], arr: List[int]) -> int:
    index = {num: i for i, num in enumerate(target)}
    dp = [float('inf')] * len(target)
    for num in arr:
        if num in index:
            i = index[num]
            dp[i] = min(dp[i], (dp[i-1] if i else 0) + 1)
    return len(target) - dp[-1]