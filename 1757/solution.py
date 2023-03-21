class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(start, end, total, res):
            if start == end:
                res.append(total)
                return
            dfs(start+1, end, total, res)
            dfs(start+1, end, total+nums[start], res)
        n = len(nums)
        left, right = [], []
        dfs(0, n//2, 0, left)
        dfs(n//2, n, 0, right)
        right.sort()
        ans = float('inf')
        for l in left:
            r = bisect_left(right, goal-l)
            if r < len(right):
                ans = min(ans, abs(goal-l-right[r]))
            if r > 0:
                ans = min(ans, abs(goal-l-right[r-1]))
        return ans