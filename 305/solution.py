class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                self.count -= 1
        parent = [-1] * (m * n)
        self.count = 0
        res = []
        for pos in positions:
            x, y = pos[0], pos[1]
            idx = x * n + y
            if parent[idx] == -1:
                parent[idx] = idx
                self.count += 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    new_idx = new_x * n + new_y
                    if 0 <= new_x < m and 0 <= new_y < n and parent[new_idx] != -1:
                        union(idx, new_idx)
            res.append(self.count)
        return res