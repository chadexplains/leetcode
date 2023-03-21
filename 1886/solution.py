class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(4):
            if mat == target:
                return True
            mat = [list(x[::-1]) for x in zip(*mat)] if i % 2 == 0 else [x[::-1] for x in mat]
        return False