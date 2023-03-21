class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        moves = 0
        max_val = -1
        for num in A:
            if num <= max_val:
                moves += max_val - num + 1
                num = max_val + 1
            max_val = num
        return moves