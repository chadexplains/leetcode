class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < abs(closest_sum - target):
                        closest_sum = s
        return closest_sum
