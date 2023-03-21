class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        current_end = 0
        farthest_end = 0
        for i in range(n-1):
            farthest_end = max(farthest_end, i + nums[i])
            if i == current_end:
                steps += 1
                current_end = farthest_end
        return steps