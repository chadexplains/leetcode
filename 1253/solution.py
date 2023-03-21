def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    n = len(colsum)
    res = [[0] * n for _ in range(2)]
    for i in range(n):
        if colsum[i] == 2:
            res[0][i] = 1
            res[1][i] = 1
            upper -= 1
            lower -= 1
    for i in range(n):
        if colsum[i] == 1:
            if upper >= lower:
                res[0][i] = 1
                upper -= 1
            else:
                res[1][i] = 1
                lower -= 1
    if upper != 0 or lower != 0 or sum(colsum) != sum(map(sum, res)):
        return []
    return res
