class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = matrix[i][0]
        for j in range(cols):
            dp[0][j] = matrix[0][j]
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return sum(sum(row) for row in dp)