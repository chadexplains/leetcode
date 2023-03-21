class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.paths = 0
        self.empty_cells = 0
        self.visited = set()
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    self.empty_cells += 1
                elif grid[i][j] == 1:
                    self.start = (i, j)
                elif grid[i][j] == 2:
                    self.end = (i, j)
        self.dfs(self.start[0], self.start[1], 0)
        return self.paths
    def dfs(self, i, j, visited_cells):
        if (i, j) == self.end and visited_cells == self.empty_cells:
            self.paths += 1
            return
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.visited and grid[x][y] != -1:
                self.visited.add((x, y))
                self.dfs(x, y, visited_cells+1)
                self.visited.remove((x, y))