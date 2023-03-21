class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        nums.sort()
        count.sort()
        res = 0
        for i in range(n):
            res += nums[i] * count[i]
        return res % (10 ** 9 + 7)