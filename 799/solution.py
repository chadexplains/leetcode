class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * (i + 1) for i in range(100)]
        glasses[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if glasses[i][j] > 1:
                    excess = glasses[i][j] - 1
                    glasses[i + 1][j] += excess / 2
                    glasses[i + 1][j + 1] += excess / 2
                    glasses[i][j] = 1
        return glasses[query_row][query_glass]