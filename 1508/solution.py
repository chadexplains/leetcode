class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for i in range(n):
            prefix_sum = 0
            for j in range(i, n):
                prefix_sum += nums[j]
                subarray_sums.append(prefix_sum)
        subarray_sums.sort()
        return sum(subarray_sums[left-1:right]) % (10**9 + 7)