class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            matrix[i].sort()
        matrix_t = [[matrix[j][i] for j in range(m)] for i in range(n)]
        for i in range(n):
            matrix_t[i].sort()
        matrix = [[matrix_t[j][i] for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                if i == 0:
                    ans = max(ans, 1)
                else:
                    matrix[i][j] += matrix[i-1][j]
                    ans = max(ans, matrix[i][j])
        return ans