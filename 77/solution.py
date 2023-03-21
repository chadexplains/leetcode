class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(combination, start):
            if len(combination) == k:
                output.append(combination[:])
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop()
        output = []
        backtrack([], 1)
        return output