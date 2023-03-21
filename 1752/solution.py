class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        pivot = min(nums)
        pivot_index = nums.index(pivot)
        if pivot_index == 0:
            return all(nums[i] <= nums[i+1] for i in range(n-1))
        elif pivot_index == n-1:
            return all(nums[i] <= nums[i+1] for i in range(n-1))
        else:
            return all(nums[i] <= nums[i+1] for i in range(pivot_index, n-1)) and all(nums[i] <= nums[i+1] for i in range(pivot_index)) and nums[-1] <= nums[0]