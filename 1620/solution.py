class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x = max(towers, key=lambda x: x[0])[0]
        max_y = max(towers, key=lambda x: x[1])[1]
        grid = [[0] * (max_y + 1) for _ in range(max_x + 1)]
        for x, y, q in towers:
            for i in range(max_x + 1):
                for j in range(max_y + 1):
                    d = ((i - x) ** 2 + (j - y) ** 2) ** 0.5
                    if d <= radius:
                        grid[i][j] += int(q / (1 + d))
        max_quality = 0
        best_coord = [0, 0]
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                quality = grid[i][j]
                if quality > max_quality:
                    max_quality = quality
                    best_coord = [i, j]
        return best_coord