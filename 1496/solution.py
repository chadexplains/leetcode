class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        curr = (0, 0)
        visited.add(curr)
        for direction in path:
            if direction == 'N':
                curr = (curr[0], curr[1] + 1)
            elif direction == 'S':
                curr = (curr[0], curr[1] - 1)
            elif direction == 'E':
                curr = (curr[0] + 1, curr[1])
            else:
                curr = (curr[0] - 1, curr[1])
            if curr in visited:
                return True
            visited.add(curr)
        return False