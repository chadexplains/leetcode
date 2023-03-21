class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0] * m for _ in range(n)]
        for ri, ci in indices:
            for j in range(m):
                matrix[ri][j] += 1
            for i in range(n):
                matrix[i][ci] += 1
        return sum(1 for row in matrix for cell in row if cell % 2 == 1)