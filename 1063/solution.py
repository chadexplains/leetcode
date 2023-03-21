class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                stack.pop()
                count += i - stack[-1] - 1 if stack else i
            stack.append(i)
        while stack:
            stack.pop()
            count += len(nums) - stack[-1] - 1 if stack else len(nums)
        return count