def knightProbability(N: int, K: int, r: int, c: int) -> float:
    dp = [[0] * N for _ in range(N)]
    dp[r][c] = 1
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for _ in range(K):
        new_dp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for dx, dy in moves:
                    x, y = i + dx, j + dy
                    if 0 <= x < N and 0 <= y < N:
                        new_dp[i][j] += dp[x][y]
        dp = new_dp
    return sum(map(sum, dp)) / (8 ** K)