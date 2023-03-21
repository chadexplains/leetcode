class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                end = mid-1
            else:
                start = mid+1
        return -1