class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            suffix[n - i - 1] = suffix[n - i] + nums[n - i - 1]
        max_sum = 0
        max_first = [0] * n
        max_second = [0] * n
        for i in range(firstLen - 1, n - secondLen):
            max_first[i] = max(max_first[i - 1], prefix[i + 1] - prefix[i + 1 - firstLen])
        for i in range(secondLen - 1, n - firstLen):
            max_second[i] = max(max_second[i - 1], suffix[i] - suffix[i + secondLen])
        for i in range(firstLen - 1, n - secondLen):
            max_sum = max(max_sum, max_first[i] + max_second[i + 1])
        for i in range(secondLen - 1, n - firstLen):
            max_sum = max(max_sum, max_first[i - 1] + max_second[i])
        return max_sum