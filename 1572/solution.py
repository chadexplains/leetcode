class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0
        for i in range(n):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[i][n - i - 1] if i != n - i - 1 else 0
        return diagonal_sum