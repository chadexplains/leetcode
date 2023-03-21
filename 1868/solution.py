def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
    i, j, m, n, res = 0, 0, len(encoded1), len(encoded2), []
    while i < m and j < n:
        a, b = encoded1[i], encoded2[j]
        val, cnt = a[1] * b[1], min(a[0], b[0])
        encoded1[i][0], encoded2[j][0] = encoded1[i][0] - cnt, encoded2[j][0] - cnt
        if encoded1[i][0] == 0: i += 1
        if encoded2[j][0] == 0: j += 1
        if not res or res[-1][1] != val: res.append([cnt, val])
        else: res[-1][0] += cnt
    return res