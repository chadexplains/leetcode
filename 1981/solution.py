class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        s = {0}
        for row in mat:
            s = {x + y for x in s for y in row}
        return min(abs(x - target) for x in s)