class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houseRobber(nums):
            prevMax = currMax = 0
            for num in nums:
                temp = currMax
                currMax = max(prevMax + num, currMax)
                prevMax = temp
            return currMax
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))