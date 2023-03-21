class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.findPeak(mountain_arr)
        left = self.binarySearch(mountain_arr, target, 0, peak)
        if left != -1:
            return left
        return self.binarySearch(mountain_arr, target, peak + 1, mountain_arr.length() - 1)

    def findPeak(self, arr):
        left, right = 0, arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if arr.get(mid) < arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearch(self, arr, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1