def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
    n = len(nums)
    freq = [0] * n
    for l, r in requests:
        freq[l] += 1
        if r+1 < n:
            freq[r+1] -= 1
    for i in range(1, n):
        freq[i] += freq[i-1]
    nums.sort(reverse=True)
    freq.sort(reverse=True)
    return sum(x * f for x, f in zip(nums, freq)) % (10**9 + 7)