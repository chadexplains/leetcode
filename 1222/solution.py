def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
    queen_set = set(tuple(q) for q in queens)
    result = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x, y = king
            while 0 <= x+dx < 8 and 0 <= y+dy < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    result.append([x, y])
                    break
    return result