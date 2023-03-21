class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        return count