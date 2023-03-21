class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def generate_subsequence(start, end, total):
            if start == end:
                return [total]
            return generate_subsequence(start+1, end, total) + generate_subsequence(start+1, end, total+nums[start])
        n = len(nums)
        left = generate_subsequence(0, n//2, 0)
        right = generate_subsequence(n//2, n, 0)
        right.sort()
        ans = float('inf')
        for l in left:
            r = bisect_left(right, goal-l)
            if r < len(right):
                ans = min(ans, abs(goal-l-right[r]))
            if r > 0:
                ans = min(ans, abs(goal-l-right[r-1]))
        return ans