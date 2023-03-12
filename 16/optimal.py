class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s
        return closest_sum
