class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        mid_row = rows[len(rows) // 2]
        mid_col = cols[len(cols) // 2]
        return sum([abs(r - mid_row) + abs(c - mid_col) for r, c in zip(rows, cols)])