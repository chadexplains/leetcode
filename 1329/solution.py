class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                diagonals[i-j].append(mat[i][j])
        for k in diagonals:
            diagonals[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i-j].pop()
        return mat