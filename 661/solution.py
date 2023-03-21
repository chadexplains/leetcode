class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count, total = 0, 0
                for r in range(max(0, i-1), min(m, i+2)):
                    for c in range(max(0, j-1), min(n, j+2)):
                        count += 1
                        total += M[r][c]
                res[i][j] = total // count
        return res