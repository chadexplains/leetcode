class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [(i - ranges[i], i + ranges[i]) for i in range(len(ranges))]
        taps.sort()
        dp = [n + 2] * (n + 1)
        dp[0] = 0
        for i in range(len(taps)):
            start, end = taps[i]
            for j in range(max(0, start), min(n, end) + 1):
                dp[j] = min(dp[j], dp[max(0, start - 1)] + 1)
        return dp[n] if dp[n] < n + 2 else -1