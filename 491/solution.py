class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, seq):
            if len(seq) > 1:
                res.append(seq)
            for i in range(start, len(nums)):
                if not seq or nums[i] >= seq[-1]:
                    backtrack(i+1, seq+[nums[i]])
        res = []
        backtrack(0, [])
        return res