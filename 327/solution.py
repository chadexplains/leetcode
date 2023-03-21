class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def mergeSort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = mergeSort(lo, mid) + mergeSort(mid, hi)
            i = j = mid
            for left in nums[lo:mid]:
                while i < hi and nums[i] - left <  lower: i += 1
                while j < hi and nums[j] - left <= upper: j += 1
                count += j - i
            nums[lo:hi] = sorted(nums[lo:hi])
            return count
        return mergeSort(0, len(nums))