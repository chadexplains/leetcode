class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        res = (1 << (n - 1)) * m
        for j in range(1, n):
            cnt = 0
            for i in range(m):
                cnt += A[i][j] == A[i][0]
            res += max(cnt, m - cnt) * (1 << (n - j - 1))
        return res