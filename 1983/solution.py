class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = float('inf')
        min_index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                diff = abs(i - start)
                if diff < min_diff:
                    min_diff = diff
                    min_index = i
        return min_diff