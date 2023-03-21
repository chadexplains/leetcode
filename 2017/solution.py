class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, diag1, diag2 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        lamps_on = set()
        for r, c in lamps:
            rows[r] += 1
            cols[c] += 1
            diag1[r-c] += 1
            diag2[r+c] += 1
            lamps_on.add((r, c))
        res = []
        for r, c in queries:
            if rows[r] > 0 or cols[c] > 0 or diag1[r-c] > 0 or diag2[r+c] > 0:
                res.append(1)
                for i, j in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                    if (i, j) in lamps_on:
                        rows[i] -= 1
                        cols[j] -= 1
                        diag1[i-j] -= 1
                        diag2[i+j] -= 1
                        lamps_on.remove((i, j))
            else:
                res.append(0)
        return res