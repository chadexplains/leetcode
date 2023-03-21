class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = [(i, j) for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j] == 0]
        for i, j in q:
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] > 2**30:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))