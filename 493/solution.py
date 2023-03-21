class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums, 0
            mid = len(nums) // 2
            left, countLeft = mergeSort(nums[:mid])
            right, countRight = mergeSort(nums[mid:])
            merged, count = merge(left, right)
            return merged, count + countLeft + countRight
        
        def merge(left, right):
            i, j, count = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= 2 * right[j]:
                    i += 1
                else:
                    count += len(left) - i
                    j += 1
            return sorted(left + right), count
        
        _, count = mergeSort(nums)
        return count