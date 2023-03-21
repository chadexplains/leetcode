class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        for i in range(n):
            for j in range(i, n):
                d = {0: 1}
                cur = 0
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    count += d.get(cur - target, 0)
                    d[cur] = d.get(cur, 0) + 1
        return count