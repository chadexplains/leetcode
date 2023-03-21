class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_val = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < min_val:
                return True
            while stack and nums[i] > stack[-1]:
                min_val = stack.pop()
            stack.append(nums[i])
        return False