class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n, l = len(A), len(B[0]), len(B)
        tableA, tableB = defaultdict(dict), defaultdict(dict)
        for i in range(m):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    tableA[i][j] = A[i][j]
        for i in range(l):
            for j in range(n):
                if B[i][j] != 0:
                    tableB[j][i] = B[i][j]
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for k, v in tableA[i].items():
                for j, w in tableB[k].items():
                    res[i][j] += v * w
        return res