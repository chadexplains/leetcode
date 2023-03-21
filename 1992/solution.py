def findFarmland(land):
    m, n = len(land), len(land[0])
    visited = set()
    groups = []
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0 or (r, c) in visited:
            return (r-1, c-1)
        visited.add((r, c))
        bottom_right = dfs(r+1, c)
        bottom_right = max(bottom_right, dfs(r, c+1), key=lambda x: (x[0], x[1]))
        return bottom_right
    
    for r in range(m):
        for c in range(n):
            if land[r][c] == 1 and (r, c) not in visited:
                top_left = (r, c)
                bottom_right = dfs(r, c)
                groups.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
    
    return groups