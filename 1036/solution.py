class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(source, target, blocked):
            q = deque([source])
            seen = set()
            seen.add(tuple(source))
            while q:
                x, y = q.popleft()
                if [x, y] == target:
                    return True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in seen and [nx, ny] not in blocked:
                        q.append((nx, ny))
                        seen.add((nx, ny))
                        if len(seen) >= 20000:
                            return True
            return False
        return bfs(source, target, blocked) and bfs(target, source, blocked)