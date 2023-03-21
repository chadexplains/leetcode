class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_perm, remaining):
            if not remaining:
                res.append(curr_perm)
                return
            for i in range(len(remaining)):
                backtrack(curr_perm + [remaining[i]], remaining[:i] + remaining[i+1:])
        res = []
        backtrack([], nums)
        return res