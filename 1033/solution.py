class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        empty_spaces = stones[2] - stones[0] - 2
        if empty_spaces == -1:
            return [0, 0]
        min_moves = empty_spaces + 1 if empty_spaces < 2 else 2
        max_moves = (stones[1] - stones[0] - 1) + (stones[2] - stones[1] - 1)
        return [min_moves, max_moves]