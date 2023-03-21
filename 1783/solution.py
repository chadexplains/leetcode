def minDifference(nums):
    sorted_nums = sorted(nums)
    median = sorted_nums[len(nums)//2]
    closest = min(sorted_nums, key=lambda x: abs(x-median))
    sorted_nums[sorted_nums.index(closest)] = median
    return max(sorted_nums) - min(sorted_nums)