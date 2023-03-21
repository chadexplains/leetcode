class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(combination, target, start):
            if target == 0:
                result.append(list(combination))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                combination.append(candidates[i])
                backtrack(combination, target - candidates[i], i)
                combination.pop()
        backtrack([], target, 0)
        return result
