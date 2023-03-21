class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        def backtrack(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            if dp[r1][c1][r2] != -1:
                return dp[r1][c1][r2]
            ans = grid[r1][c1]
            if r1 != r2:
                ans += grid[r2][c2]
            ans += max(backtrack(r1+1, c1, r2+1), backtrack(r1, c1+1, r2+1), backtrack(r1+1, c1, r2), backtrack(r1, c1+1, r2))
            dp[r1][c1][r2] = ans
            return ans
        return max(0, backtrack(0, 0, 0))