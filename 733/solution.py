def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    color = image[sr][sc]
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != color:
            return
        image[r][c] = newColor
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
    dfs(sr, sc)
    return image