def checkMove(board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for d in directions:
        r, c = rMove + d[0], cMove + d[1]
        count = 0
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == color:
                return True if count > 0 else False
            elif board[r][c] != '.':
                break
            r, c = r + d[0], c + d[1]
            count += 1
    return False