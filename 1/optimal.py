class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
