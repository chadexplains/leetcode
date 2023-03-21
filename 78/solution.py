class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        def backtrack(temp, start):
            subsets.append(temp[:])
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(temp, i + 1)
                temp.pop()
        backtrack([], 0)
        return subsets