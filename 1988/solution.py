class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(mat[i][j] * (1 << (i * n + j)) for i in range(m) for j in range(n))
        q, visited = deque([(start, 0)]), set([start])
        while q:
            state, steps = q.popleft()
            if state == 0:
                return steps
            for i in range(m):
                for j in range(n):
                    new_state = state
                    for ni, nj in [(i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= ni < m and 0 <= nj < n:
                            bit = ni * n + nj
                            new_state ^= 1 << bit
                    if new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, steps + 1))
        return -1