class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sums = {0: -1}
        count = 0
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            if sum - target in sums:
                count += 1
                sum = 0
                sums = {0: -1}
            else:
                sums[sum] = i
        return count