class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        diagonals = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+j not in diagonals:
                    diagonals[i+j] = [matrix[i][j]]
                else:
                    diagonals[i+j].append(matrix[i][j])
        res = []
        for k in range(len(diagonals)):
            if k % 2 == 0:
                res.extend(diagonals[k][::-1])
            else:
                res.extend(diagonals[k])
        return res
