class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(combination, curr_sum, index):
            if len(combination) == k and curr_sum == n:
                result.append(combination[:])
                return
            if curr_sum > n or len(combination) > k:
                return
            for i in range(index, 10):
                combination.append(i)
                backtrack(combination, curr_sum + i, i + 1)
                combination.pop()
        result = []
        backtrack([], 0, 1)
        return result