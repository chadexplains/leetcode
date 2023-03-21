class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            ans += sum(num & 1 for num in nums)
            nums = [(num - 1) // 2 for num in nums]
        return ans