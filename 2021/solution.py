class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        prefix = [[0] * (n + 2) for _ in range(m + 2)]
        rhombus_sums = set()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = grid[i - 1][j - 1] + prefix[i - 1][j - 1] + prefix[i][j - 1] - prefix[i - 1][j - 2]
                rhombus_sums.add(grid[i - 1][j - 1])
                for k in range(3, min(m - i + 2, n - j + 2) + 1, 2):
                    rhombus_sum = prefix[i + k - 2][j + k - 1] - prefix[i - 1][j - 1] + prefix[i + k - 1][j + k - 2] - prefix[i - 1][j - 2]
                    rhombus_sums.add(rhombus_sum)
        return sorted(rhombus_sums, reverse=True)[:3]