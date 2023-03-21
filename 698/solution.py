class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False
        nums.sort(reverse = True)
        if nums[0] > target: return False
        def dfs(groups):
            if not nums: return True
            v = nums.pop(0)
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dfs(groups): return True
                    groups[i] -= v
                if not group: break
            nums.insert(0, v)
            return False
        return dfs([0] * k)