class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]
        for i in range(1, len(jobs)):
            start, end, p = jobs[i]
            # binary search to find the latest job that ends before the current job starts
            l, r = 0, i - 1
            while l <= r:
                mid = (l + r) // 2
                if jobs[mid][1] <= start:
                    l = mid + 1
                else:
                    r = mid - 1
            # calculate the maximum profit at this job
            dp[i] = max(dp[i - 1], p + dp[r] if r >= 0 else p)
        return dp[-1]