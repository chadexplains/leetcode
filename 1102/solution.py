class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        def dfs(i, j, score):
            if i == R-1 and j == C-1:
                return True
            visited.add((i, j))
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < R and 0 <= y < C and (x, y) not in visited and A[x][y] >= score:
                    if dfs(x, y, score):
                        return True
            return False
        R, C = len(A), len(A[0])
        l, r = 0, max(max(row) for row in A)
        while l < r:
            mid = (l + r + 1) // 2
            visited = set()
            if dfs(0, 0, mid):
                l = mid
            else:
                r = mid - 1
        return l