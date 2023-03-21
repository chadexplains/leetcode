class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            longest = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    longest = max(longest, dfs(x, y) + 1)
            memo[(i, j)] = longest
            return longest
        return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))