class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False
        n = len(nums)
        nums.sort()
        used = [False] * n
        res = []
        backtrack([])
        return res