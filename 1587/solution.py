class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        for l, r in requests:
            count[l] += 1
            if r + 1 < n:
                count[r + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        nums.sort()
        count.sort()
        return sum(num * c for num, c in zip(nums, count)) % (10 ** 9 + 7)