class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, left):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid+1
            return lo
        left_idx = binarySearch(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, binarySearch(nums, target, False)-1]