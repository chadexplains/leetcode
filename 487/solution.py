class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = max_ones = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_ones = max(max_ones, right - left + 1)
        return max_ones